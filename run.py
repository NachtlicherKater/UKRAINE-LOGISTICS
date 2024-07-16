import asyncio
import Flask


from aiogram import Bot, Dispatcher
from app.handlers import router

bot = Bot(token='7132749035:AAFWm5wJhoeIihY1mwUWyr2ZktFaKMecfUI')
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except  KeyboardInterrupt:
        print('Exit')
