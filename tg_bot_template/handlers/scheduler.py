from aiogram import Bot
from lexicon.common import COMMON
from keybords.keyboard import go_kb


async def send_schedule(bot: Bot):
    await bot.send_message(text=COMMON['go'], reply_markup=go_kb())
