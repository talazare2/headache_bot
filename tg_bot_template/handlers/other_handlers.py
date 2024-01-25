from aiogram import Router
from aiogram.types import Message
from lexicon.common import COMMON



router = Router()

@router.message()
async def send_echo(message: Message):
        await message.answer(text=COMMON['?'])