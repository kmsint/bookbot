from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bookbot.services.file_handling import book
from bookbot.services.lexicon import LEXICON


def create_bookmarks_keyboard(*args):
    bookmarks_kb = InlineKeyboardMarkup()
    for button in sorted(args):
        bookmarks_kb.add(InlineKeyboardButton(text=f'{button} - {book[button][:100]}...', callback_data=button))
    bookmarks_kb.add(InlineKeyboardButton(text=LEXICON['edit_bookmarks_button'], callback_data='edit_bookmarks'),
                     InlineKeyboardButton(text=LEXICON['cancel'], callback_data='cancel'))
    return bookmarks_kb


def create_edit_keyboard(*args):
    bookmarks_kb = InlineKeyboardMarkup()
    for button in sorted(args):
        bookmarks_kb.add(InlineKeyboardButton(text=f'{LEXICON["del"]} {button} - {book[button][:100]}...', callback_data=f'{button} del'))
    bookmarks_kb.add(InlineKeyboardButton(text=LEXICON['cancel'], callback_data='cancel'))
    return bookmarks_kb