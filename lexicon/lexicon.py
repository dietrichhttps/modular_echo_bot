import os
from .lexicon_methods import get_text

# Получение абсолютного пути к папке с лексиконом
LEXICON_DIR = os.path.dirname(os.path.abspath(__file__))

# Создание словаря с путями к текстовым файлам
LEXICON_RU = {
    '/start': get_text(os.path.join(LEXICON_DIR, 'ru/start.txt')),
    '/help': get_text(os.path.join(LEXICON_DIR, 'ru/help.txt')),
    'no_echo': get_text(os.path.join(LEXICON_DIR, 'ru/no_echo.txt')),
}
