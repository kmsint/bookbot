import asyncio
import logging

from aiogram import Bot, Dispatcher

from bookbot.config import load_config
from bookbot.handlers.user import register_user_handlers
from bookbot.handlers.echo import register_echo_handler
from bookbot.keyboards.main_menu import set_main_menu


logger = logging.getLogger(__name__)


def register_all_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)
    register_echo_handler(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Starting bot')
    config = load_config()

    bot = Bot(token=config.token, parse_mode='HTML')
    dp = Dispatcher(bot)


    # await set_main_menu(bot)
    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await bot.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped!')
