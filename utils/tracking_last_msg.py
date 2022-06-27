import asyncio
import datetime

from loader import dp
from database import getters, setters


async def tracking_last_msg():
    '''Отслеживание даты последнего сообщения'''
    await asyncio.sleep(2)

    while True:
        users = await getters.get_users()

        for user in users:
            date_last_msg = datetime.datetime.strptime(user['date_last_msg'],
                '%Y-%m-%d %H:%M:%S')
            diff_time = (datetime.datetime.now() - date_last_msg).seconds / 60

            if diff_time > 10: # Если 10 минут пользователь ничего не пишет, то ему приходит уведомление. 
                print(f'Отправил сообщение {user["user_id"]}!')
                await dp.bot.send_message(user['user_id'],
                    'Вы обо мне забыли?')
                await setters.update_date_last_msg(user['user_id'])

        await asyncio.sleep(1)


asyncio.ensure_future(tracking_last_msg())