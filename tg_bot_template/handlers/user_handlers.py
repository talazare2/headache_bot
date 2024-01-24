from datetime import date

from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import CallbackQuery, Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from lexicon.lexicon import LEXICON, BUTTONS
from lexicon.common import COMMON
from lexicon.dialogs_tgbot import DIALOG
from keybords.keyboard import create_inline_kb as kb
from keybords.keyboard import yes_no_kb, loc_kb
from config_data.paths import path_to_img
from database.fsm import usr_dict, FSMFillForm
from filters.filters import FilterAD
from external.weather_api import meteo_api


#Initialize router
router = Router()

# Set default language
lang = 'ru'

# This handler reacts to /start
@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await state.clear()
    keyboard = kb(3, COMMON['en'], COMMON['ru'], COMMON['fr'])
    await message.answer(text=COMMON['/start'], reply_markup=keyboard)
    await state.set_state(FSMFillForm.fill_lang)


# This handler reacts to /abort
@router.message(Command(commands='abort'), StateFilter(default_state))
async def process_stop_command(message: Message):
    await message.answer(text=LEXICON[lang]['/abort'])


# This handler reacts to /abort, store data to db and turn off FSM
@router.message(Command(commands='abort'), ~StateFilter(default_state))
async def process_stop_command(message: Message,  state: FSMContext):
    usr_dict[message.from_user.id] = await state.get_data()
    await message.answer(text=LEXICON[lang]['/abort'])
    await state.clear()


# This handler reacts to  /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON[lang]['/help'])


# This handler allows to choose language
@router.callback_query(StateFilter(FSMFillForm.fill_lang), 
                       F.data.in_([COMMON['ru'],
                                   COMMON['en'],
                                   COMMON['fr']]))
async def process_lang_press(callback: CallbackQuery, state: FSMContext):
    global lang 
    if callback.data == COMMON['ru']:
        lang = 'ru'
        await callback.answer(text=COMMON['set_ru'], show_alert=True)
    elif callback.data == COMMON['en']:
        lang = 'en'
        await callback.answer(text=COMMON['set_en'], show_alert=True)
    elif callback.data == COMMON['fr']:
        lang = 'fr'
        await callback.answer(text=COMMON['set_fr'], show_alert=True)
    keyboard = kb(2, LEXICON[lang]['begin'], LEXICON[lang]['stop'])
    ident = callback.from_user.id
    await state.update_data(user_id = ident)
    await state.update_data(lang = lang)
    await state.update_data(date = str(date.today()))
    await callback.message.answer(text=DIALOG[lang]['intro'], reply_markup=keyboard)
    await callback.answer()
    await state.set_state(FSMFillForm.fill_start)


# This handler for exit if one doesn't want to do questionnary
@router.callback_query(StateFilter(FSMFillForm.fill_start),
                       F.data.in_([LEXICON['ru']['stop'],
                                   LEXICON['en']['stop'],
                                   LEXICON['fr']['stop']]))
async def process_stop_press(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=LEXICON[lang]['/abort'])
    await callback.answer()
    await state.clear()


# This handler ask headache level
@router.callback_query(StateFilter(FSMFillForm.fill_start), 
                       F.data.in_([LEXICON['ru']['begin'],
                                   LEXICON['en']['begin'],
                                   LEXICON['fr']['begin']]))
async def process_begin_press(callback: CallbackQuery, state: FSMContext):
    keyboard = kb(3, BUTTONS['btn0'], BUTTONS['btn1'], BUTTONS['btn2'],\
                 BUTTONS['btn3'],BUTTONS['btn4'],BUTTONS['btn5'])
    await callback.message.answer(text=DIALOG[lang]['lvl'], reply_markup=keyboard)
    await callback.answer()
    await state.set_state(FSMFillForm.fill_lvl)


# This handler ask headache location
@router.callback_query(StateFilter(FSMFillForm.fill_lvl),
                       F.data != BUTTONS['btn0'])
async def process_lvl_press(callback: CallbackQuery,  state: FSMContext):
    print('process_lvl_press', callback.data)
    await state.update_data(halvl = callback.data)
    keyboard = kb(3, BUTTONS['btn1'], BUTTONS['btn2'], BUTTONS['btn3'],\
                 BUTTONS['btn4'],BUTTONS['btn5'],BUTTONS['btn6'])
    await callback.message.answer_photo(FSInputFile(path=path_to_img), \
                                        caption=DIALOG[lang]['localisation'], reply_markup=keyboard)    
    await callback.answer()
    await state.set_state(FSMFillForm.fill_loc)


# This handler ask if it's left or right side
@router.callback_query(StateFilter(FSMFillForm.fill_loc))
async def process_loc_press(callback: CallbackQuery, state: FSMContext):
    print('process_loc_press', callback.data)
    await state.update_data(loc = callback.data)
    keyboard = kb(3, LEXICON[lang]['left'], LEXICON[lang]['right'], LEXICON[lang]['centr'])
    await callback.message.answer(text=DIALOG[lang]['lr'], reply_markup=keyboard)
    await callback.answer()
    await state.set_state(FSMFillForm.fill_side)


# This handler ask about alcohol
@router.callback_query(StateFilter(FSMFillForm.fill_side))
#this decorator allows us to skip location questions 
@router.callback_query(StateFilter(FSMFillForm.fill_lvl),
                       F.data == BUTTONS['btn0'])
async def process_lr_press(callback: CallbackQuery, state: FSMContext):
    print('process_lr_press', callback.data)
    if callback.data == BUTTONS['btn0']:
        await state.update_data(halvl = callback.data)
        await state.update_data(loc = 'NaN')
        await state.update_data(side = 'NaN')
    else:
        await state.update_data(side = callback.data)
    keyboard = kb(2, LEXICON[lang]['yes'], LEXICON[lang]['no'])
    await callback.message.answer(text=DIALOG[lang]['alcohol'], reply_markup=keyboard)
    await callback.answer()
    await state.set_state(FSMFillForm.fill_alc)


# This handler ask if you can measure blood pressure
@router.callback_query(StateFilter(FSMFillForm.fill_alc))
async def process_alc_press(callback: CallbackQuery, state: FSMContext):
    if callback.data == LEXICON[lang]['yes']:
        await state.update_data(alc = 1)
    else:
        await state.update_data(alc = 0)
    await callback.message.answer(text=DIALOG[lang]['pres_yn'], reply_markup=yes_no_kb(lang))
    await callback.answer()
    await state.set_state(FSMFillForm.fill_presyn)


# This handler ask to enter blood pressure measuremnts or give you instructions
@router.message(StateFilter(FSMFillForm.fill_presyn), F.text == LEXICON[lang]['yep'])
async def process_pr_y_n_press(message: Message, state: FSMContext):
    keyboard = kb(1, LEXICON[lang]['instr'])
    await message.answer(text=DIALOG[lang]['press_dat'], reply_markup=keyboard)
    await state.set_state(FSMFillForm.fill_press)


# This handler shows instruction    
@router.callback_query(F.data == LEXICON[lang]['instr'])
async def process_instr_press(callback: CallbackQuery):
    await callback.message.answer(text=DIALOG[lang]['instr'])
    await callback.answer()


# This handler register your blood pressure and ask about fever
@router.message(StateFilter(FSMFillForm.fill_press, ),
                FilterAD())
# This decorator allows to pass BP measurements
@router.message(StateFilter(FSMFillForm.fill_presyn), 
                       F.text == LEXICON[lang]['nope'])
async def process_ad_press(message: Message, state: FSMContext):
    await state.update_data(ad = message.text)
    keyboard = kb(1, LEXICON[lang]['le372'],LEXICON[lang]['le385'], LEXICON[lang]['mo385'])
    await message.answer(text=DIALOG[lang]['fever'], reply_markup=keyboard)
    await state.set_state(FSMFillForm.fill_fev)


@router.message(StateFilter(FSMFillForm.fill_press),
                ~FilterAD())
async def process_ad_press_bad(message: Message, state: FSMContext):
    await message.answer(text=LEXICON[lang]['wr_for'])

# This handler asks how did you sleep
@router.callback_query(StateFilter(FSMFillForm.fill_fev))
async def process_fev_press(callback: CallbackQuery, state: FSMContext):
    if callback.data == LEXICON[lang]['le372']:
        await state.update_data(fever = 0)   
    elif callback.data == LEXICON[lang]['le385']:
        await state.update_data(fever = 1)
    else:
        await state.update_data(fever = 2)
    keyboard = kb(3, BUTTONS['btn0'], BUTTONS['btn1'], BUTTONS['btn2'],\
                  BUTTONS['btn3'],BUTTONS['btn4'],BUTTONS['btn5'])    
    await callback.message.answer(text=DIALOG[lang]['sleep'], reply_markup=keyboard)
    await callback.answer()
    await state.set_state(FSMFillForm.fill_sleep)


# This handler asks to provide geolocalisation
@router.callback_query(StateFilter(FSMFillForm.fill_sleep))
async def process_sleep_press(callback: CallbackQuery, state: FSMContext):
    await state.update_data(sleep = callback.data)
    await callback.message.answer(text=DIALOG[lang]['meteo'], reply_markup=loc_kb(lang))
    await callback.answer()
    await state.set_state(FSMFillForm.fill_meteo)


@router.message(StateFilter(FSMFillForm.fill_meteo))
async def process_location(message: Message, state: FSMContext):
    api_text, met_code_list =  meteo_api(message.location.latitude, message.location.longitude, lang)
    await state.update_data(t_max = met_code_list[0])
    await state.update_data(t_min = met_code_list[1])
    await state.update_data(precip = met_code_list[2])
    await state.update_data(wind_force = met_code_list[3])
    await state.update_data(wind_dir = met_code_list[4])
    meteo_text = DIALOG[lang]['met_true']
    meteo_text += api_text
    await message.answer(text=meteo_text)

