import datetime

from .work_db import *


async def add_new_user(user_data):
    '''Добавление нового пользователя в БД'''
    query = '''
    INSERT INTO users
        (user_id, date_last_msg)
    VALUES
        (?, ?);
    '''

    await execute_query(query, user_data)


async def update_date_last_msg(user_id):
    '''Обновлении даты и времени последнего сообщения пользователя'''
    query = '''
    UPDATE
        users
    SET
        date_last_msg = ?
    WHERE
        user_id = ?
    '''

    await execute_query(query,
        [datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), user_id])