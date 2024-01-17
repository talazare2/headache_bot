from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon.lexicon import LEXICON, BUTTONS
from lexicon.common import COMMON
from lexicon.lang import lang
from lexicon.dialogs_tgbot import DIALOG
from keybords.keyboard import create_inline_kb as kb
from database.database import df_headache


#Initialize router
router = Router()



# This handler reacts to /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    keyboard = kb(3, COMMON['en'], COMMON['ru'], COMMON['fr'])
    await message.answer(text=COMMON['/start'], reply_markup=keyboard)

@router.message(F.text == COMMON['ru'])
async def process_ru_answer(message: Message):
    print('language chosen ru')
    global lang 
    lang = 'ru'
    await message.answer(text=COMMON['set_ru'])
    keybord = kb(3, BUTTONS['btn0'], BUTTONS['btn1'], BUTTONS['btn2'],\
                 BUTTONS['btn3'],BUTTONS['btn4'],BUTTONS['btn5'])
    await message.answer(text=DIALOG['Hello'], reply_markup=keybord)

@router.message(F.text == COMMON['en'])
async def process_en_answer(message: Message):
    print('language chosen en')
    global lang 
    lang = 'en'
    await message.answer(text=COMMON['set_en'])
    keybord = kb(3, BUTTONS['btn0'], BUTTONS['btn1'], BUTTONS['btn2'],\
                 BUTTONS['btn3'],BUTTONS['btn4'],BUTTONS['btn5'])
    await message.answer(text=DIALOG['Hello'], reply_markup=keybord)

@router.message(F.text == COMMON['fr'])
async def process_fr_answer(message: Message):
    print('language chosen fr')
    global lang 
    lang = 'fr'
    await message.answer(text=COMMON['set_fr'])
    keybord = kb(3, BUTTONS['btn0'], BUTTONS['btn1'], BUTTONS['btn2'],\
                 BUTTONS['btn3'],BUTTONS['btn4'],BUTTONS['btn5'])
    await message.answer(text=DIALOG['Hello'], reply_markup=keybord)

# This handler reacts to  /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'])