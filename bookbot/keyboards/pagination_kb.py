from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bookbot.services.lexicon import LEXICON


# Функция, генерирующая клавиатуру для страницы книги
def create_pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    pagination_kb = InlineKeyboardMarkup()
    pagination_kb.row(*[InlineKeyboardButton(LEXICON[button] if button in LEXICON else button,
                      callback_data=button) for button in buttons])
    return pagination_kb