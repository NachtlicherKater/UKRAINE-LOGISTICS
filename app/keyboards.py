from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='11')],
    [KeyboardButton(text='22'), KeyboardButton(text='22')]
])
