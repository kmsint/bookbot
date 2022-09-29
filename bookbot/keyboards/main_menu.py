from aiogram import Bot, types


async def set_main_menu(bot: Bot):
    cmds = [
        types.BotCommand('/beginning', 'В начало книги'),
        types.BotCommand('/continue', 'Продолжить чтение'),
        types.BotCommand('/bookmarks', 'Мои закладки'),
        types.BotCommand('/help', 'Справка по работе бота')
    ]
    await bot.set_my_commands(cmds)
