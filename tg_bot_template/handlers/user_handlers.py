from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from datetime import datetime

from lexicon.lexicon import LEXICON, BUTTONS
from lexicon.common import COMMON
from lexicon.lang import lang
from lexicon.dialogs_tgbot import DIALOG
from keybords.keyboard import create_inline_kb as kb
from database.database import df_headache, df_dict


#Initialize router
router = Router()



# This handler reacts to /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    keyboard = kb(3, COMMON['en'], COMMON['ru'], COMMON['fr'])
    await message.answer(text=COMMON['/start'], reply_markup=keyboard)


# This handler reacts to /abort
@router.message(Command(commands='abort'))
async def process_stop_command(message: Message):
    await message.answer(text=LEXICON['/abort'])

@router.callback_query(F.data == COMMON['ru'])
async def process_ru_press(callback: CallbackQuery):
    global lang 
    lang = 'ru'
    await callback.answer(text=COMMON['set_ru'], show_alert=True, )
    keyboard = kb(2, LEXICON['begin'], LEXICON['stop'])
    await callback.message.answer(text=DIALOG['intro'], reply_markup=keyboard)

@router.callback_query(F.data == COMMON['en'])
async def process_en_press(callback: CallbackQuery):
    global lang 
    lang = 'en'
    keyboard = kb(2, LEXICON['begin'], LEXICON['stop'])
    await callback.answer(text=COMMON['set_en'], show_alert=True)
    await callback.message.answer(text=DIALOG['intro'], reply_markup=keyboard)

@router.callback_query(F.data == COMMON['fr'])
async def process_fr_press(callback: CallbackQuery):
    global lang 
    lang = 'fr'
    keyboard = kb(2, LEXICON['begin'], LEXICON['stop'])
    await callback.answer(text=COMMON['set_fr'], show_alert=True)
    await callback.message.answer(text=DIALOG['intro'], reply_markup=keyboard)

@router.callback_query(F.data == LEXICON['begin'])
async def process_begin_press(callback: CallbackQuery):
    keyboard = kb(3, BUTTONS['btn0'], BUTTONS['btn1'], BUTTONS['btn2'],\
                 BUTTONS['btn3'],BUTTONS['btn4'],BUTTONS['btn5'])
    await callback.message.answer(text=DIALOG['lvl'], reply_markup=keyboard)

@router.callback_query(F.data == LEXICON['stop'])
async def process_begin_press(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON['/abort'])


@router.callback_query(F.data)
async def process_lvl_press(callback: CallbackQuery):
    df_headache[lvl].
    keyboard = kb(3, BUTTONS['btn0'], BUTTONS['btn1'], BUTTONS['btn2'],\
                 BUTTONS['btn3'],BUTTONS['btn4'],BUTTONS['btn5'])
    await callback.message.answer(text=DIALOG['lvl'], reply_markup=keyboard)



# This handler reacts to  /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'])