from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def other_message(message: Message):
    await message.answer(f'Я не понимаю команду {message.text}.\nДля получения списка доступных команд используй /help')