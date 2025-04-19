from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import logging
import os

API_TOKEN = '7733383691:AAEtqFuM5Z5OwOPLWpL97GyiiZzDrGYaxlU'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("Bot ishga tushdi va tayyor!")

async def send_text_to_chat(text: str, chat_id: int):
    await bot.send_message(chat_id=chat_id, text=text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
