import asyncio, aiohttp


from aiogram import Bot, Dispatcher
from app.handlers import router

bot = Bot(token='7132749035:AAF9o3HI3O-eI1PFyRXsuroeQhNSFWxryTo')
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except  KeyboardInterrupt:
        print('Exit')
