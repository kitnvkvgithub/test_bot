from aiogram import types

from loader import dp
from database import setters


@dp.message_handler()
async def echo(message: types.Message):
    '''Ответ на сообщение'''
    await setters.update_date_last_msg(message.from_user.id)
    await message.reply(message.text)