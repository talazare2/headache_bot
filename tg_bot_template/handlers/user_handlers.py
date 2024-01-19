from datetime import date

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message, FSInputFile

from lexicon.lexicon import LEXICON, BUTTONS_LVL, BUTTONS_LOC, BUTTONS_SLEEP
from lexicon.common import COMMON
from lexicon.dialogs_tgbot import DIALOG
from keybords.keyboard import create_inline_kb as kb
from database.day_dict import df_dict
from config_data.paths import path_to_img


#Initialize router
router = Router()

# Set default language
lang = 'ru'

# This handler reacts to /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    keyboard = kb(3, COMMON['en'], COMMON['ru'], COMMON['fr'])
    await message.answer(text=COMMON['/start'], reply_markup=keyboard)
# This handler reacts to /abort
@router.message(Command(commands='abort'))
async def process_stop_command(message: Message):
    await message.answer(text=LEXICON[lang]['/abort'])


# This handler reacts to  /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON[lang]['/help'])


# This handler allows to choose language
@router.callback_query(F.data.in_([COMMON['ru'],
                                   COMMON['en'],
                                   COMMON['fr']]))
async def process_lang_press(callback: CallbackQuery):
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
    await callback.message.answer(text=DIALOG[lang]['intro'], reply_markup=keyboard)
    await callback.answer()


# This handler ask headache level
@router.callback_query(F.data.in_([LEXICON['ru']['begin'],
                                   LEXICON['en']['begin'],
                                   LEXICON['fr']['begin']]))
async def process_begin_press(callback: CallbackQuery):
    keyboard = kb(3, BUTTONS_LVL['btn0'], BUTTONS_LVL['btn1'], BUTTONS_LVL['btn2'],\
                 BUTTONS_LVL['btn3'],BUTTONS_LVL['btn4'],BUTTONS_LVL['btn5'])
    await callback.message.answer(text=DIALOG[lang]['lvl'], reply_markup=keyboard)


# This handler for exit if one doesn't want to do questionnary
@router.callback_query(F.data.in_([LEXICON['ru']['stop'],
                                   LEXICON['en']['stop'],
                                   LEXICON['fr']['stop']]))
async def process_stop_press(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON[lang]['/abort'])


# This handler ask headache location
@router.callback_query(F.data.in_([BUTTONS_LVL['btn1'], BUTTONS_LVL['btn2'], BUTTONS_LVL['btn3'],
                                   BUTTONS_LVL['btn4'],BUTTONS_LVL['btn5']]))
async def process_lvl_press(callback: CallbackQuery):
    df_dict['date'] = str(date.today())
    df_dict['halvl'] = callback.data
    keyboard = kb(3, BUTTONS_LOC['bt1'], BUTTONS_LOC['bt2'], BUTTONS_LOC['bt3'],\
                 BUTTONS_LOC['bt4'],BUTTONS_LOC['bt5'],BUTTONS_LOC['bt6'])
    await callback.message.answer_photo(FSInputFile(path=path_to_img), caption=DIALOG[lang]['localisation'], reply_markup=keyboard)


# This handler ask if it's left or right side
@router.callback_query(F.data.in_([BUTTONS_LOC['bt1'], BUTTONS_LOC['bt2'], BUTTONS_LOC['bt3'],
                                   BUTTONS_LOC['bt4'],BUTTONS_LOC['bt5'],BUTTONS_LOC['bt6']]))
async def process_loc_press(callback: CallbackQuery):
    df_dict['loc'] = callback.data
    keyboard = kb(3, LEXICON[lang]['left'], LEXICON[lang]['right'], LEXICON[lang]['centr'])
    await callback.message.answer(text=DIALOG[lang]['lr'], reply_markup=keyboard)


# This handler ask about alcohol
@router.callback_query(F.data.in_([BUTTONS_LVL['btn0'], LEXICON[lang]['left'], 
                                   LEXICON[lang]['right'], LEXICON[lang]['centr']]))
async def process_lr_press(callback: CallbackQuery):
    if callback.data == BUTTONS_LVL['btn0']:
        df_dict['loc'] == callback.data
    elif callback.data == LEXICON[lang]['left']:
        df_dict['loc'] += '1'
    elif callback.data == LEXICON[lang]['right']:
        df_dict['loc'] += '2'
    elif callback.data == LEXICON[lang]['cernt']:
        df_dict['loc'] += '3'
    keyboard = kb(3, LEXICON[lang]['yes'], LEXICON[lang]['no'])
    await callback.message.answer(text=DIALOG[lang]['alcohol'], reply_markup=keyboard)