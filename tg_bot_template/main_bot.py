import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis
from config_data.config import Config, load_config
from handlers import user_handlers
from config_data.paths import path_to_env
#logging initialization
logger = logging.getLogger(__name__)


# Config and launch bot
async def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Print bot status in the terminal
    logger.info('Starting bot')
    logger.setLevel(logging.DEBUG)
    # Load config
    config: Config = load_config(path_to_env)

    redis = Redis(host='localhost')
    storage = RedisStorage(redis=redis)

    # Initialize bot (html for text formatting)
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(storage=storage)

    # Register router
    dp.include_router(user_handlers.router)

    # Skip update, launch polling
    await bot.delete_webhook(drop_pending_updates=False)
    await dp.start_polling(bot, allowed_updates=[])



if __name__ == '__main__':
    asyncio.run(main())
