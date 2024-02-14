from lexicon_methods import get_text

LEXICON_RU: dict[str: get_text] = {
    '/start': get_text('ru/start.txt'),
    '/help': get_text('ru/help.txt'),
    'no_echo': get_text('ru/no_echo.txt'),
}