import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

# Bot tokeningizni shu yerga kiriting
TOKEN = "7713335011:AAFhULFxPo1Ix6lkeMDXZo8Z4XDddJzO-lE"

# Logger sozlamalari
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher yaratish
bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start va /help buyruqlariga javob beruvchi handler
@dp.message(Command("start", "help"))
async def start_handler(message: Message):
    await message.answer("Salom! Men aiogram 3.18 bilan yozilgan botman! 😊")

# Har qanday xabarga javob beruvchi handler (echo)
@dp.message()
async def echo_handler(message: Message):
    await message.answer(message.text)

# Asosiy ishga tushirish funksiyasi
async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

# Botni ishga tushirish
if __name__ == "__main__":
    asyncio.run(main())
