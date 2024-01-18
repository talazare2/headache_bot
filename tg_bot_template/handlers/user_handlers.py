from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from datetime import date

from lexicon.lexicon import LEXICON, BUTTONS
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

@router.callback_query(F.data.in_([LEXICON['ru']['begin'],
                                   LEXICON['en']['begin'],
                                   LEXICON['fr']['begin']]))
async def process_begin_press(callback: CallbackQuery):
    keyboard = kb(3, BUTTONS['btn0'], BUTTONS['btn1'], BUTTONS['btn2'],\
                 BUTTONS['btn3'],BUTTONS['btn4'],BUTTONS['btn5'])
    await callback.message.answer(text=DIALOG[lang]['lvl'], reply_markup=keyboard)

@router.callback_query(F.data.in_([LEXICON['ru']['stop'],
                                   LEXICON['en']['stop'],
                                   LEXICON['fr']['stop']]))
async def process_stop_press(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON[lang]['/abort'])


@router.callback_query(F.data.in_([BUTTONS['btn0'], BUTTONS['btn1'], BUTTONS['btn2'],
                                   BUTTONS['btn3'],BUTTONS['btn4'],BUTTONS['btn5']]))
async def process_lvl_press(callback: CallbackQuery):
    df_dict['date'] = str(date.today())
    df_dict['halvl'] = callback.data
    keyboard = kb(3, BUTTONS['btn1'], BUTTONS['btn2'], BUTTONS['btn3'],\
                 BUTTONS['btn4'],BUTTONS['btn5'],BUTTONS['btn6'])
    await callback.message.answer_photo(types.FSInputFile(path=path_to_img), caption=DIALOG[lang]['localisation'], reply_markup=keyboard)



# This handler reacts to  /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON[lang]['/help'])