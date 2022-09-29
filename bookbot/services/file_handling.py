BOOK_PATH = 'bookbot/book/Bredberi_Zarubezhnaya-fantastika-izd-vo-Mir-_1965_Marsianskie-hroniki.512795.txt'
# BOOK_PATH = 'bookbot/book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text : str, start: int, size: int) -> tuple[str, int]:
    end_signs = ',.!:;?'
    counter = 0
    if len(text) < start + size:
        size = len(text) - start
        text = text[start:start + size]
    else:
        text = text[start:start + size]
        for i in range(size - 1, 0, -1):
            if text[i] in end_signs:
                break
            counter = size - i
    page_text = text[:size - counter]
    page_size = size - counter
    return page_text, page_size  


def prepare_book(path: str) -> None:
    with open(path, 'r') as file:
        text = file.read()
        start = 0
        page_number = 1
        while start < len(text):
            page_text, page_size = _get_part_text(text, start, PAGE_SIZE)
            start += page_size
            book[page_number] = page_text.strip()
            page_number += 1


prepare_book(BOOK_PATH)

print(book)