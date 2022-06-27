import datetime

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from database import getters, setters


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    '''Запуск бота'''
    user_id = message.from_user.id
    user_data = await getters.get_user_data(user_id)

    if not user_data:
        user_data = (
            user_id,
            message.date,
        )
        await setters.add_new_user(user_data)

    await message.answer('Привет!')