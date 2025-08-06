import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from googletrans import Translator
import os
import dotenv

load_dotenv()
token = os.getenv("TOKEN")
TOKEN = token

bot = Bot(token=TOKEN)
dp = Dispatcher()
translator = Translator()


@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет! Отправь мне текст на русском, я переведу его на английский.")


@dp.message()
async def translate_text(message: types.Message):
    text = message.text
    # Определяем язык
    detected = translator.detect(text)

    if detected.lang == 'ru':  # Если русский
        translated = translator.translate(text, src='ru', dest='en')
        await message.answer(f"**Перевод:** {translated.text}")
    else:
        await message.answer("Ошибка: поддерживается только русский текст.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
