from aiogram import F, Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hi bitch!')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'id photo: {message.photo[-1].file_id}')

@router.message(Command('фото_профиля'))
async def photo_profile(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMtZpWRJSCEf1tI5mHzsulvJzj7P44AAgvnMRuYz7BIEkWdaXRkBpgBAAMCAAN5AAM1BA',
                               caption='Вот фото с профиля сервера!')

@router.message(Command('правила'))
async def photo_profile(message: Message):
    await message.answer('https://discord.com/channels/1231989038110740510/1231989038311805091')

@router.message(F.text == '1')
async def shto(message: Message):
    await message.answer('2')

@router.message(F.text == 'Курва')
async def shto(message: Message):
    await message.answer('Бобер! Я пьердоле!')
