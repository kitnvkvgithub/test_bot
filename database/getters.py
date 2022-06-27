from .work_db import *


async def get_user_data(user_id):
    '''Возвращает данные пользователя'''
    query = '''
    SELECT
        *
    FROM
        users
    WHERE
        user_id = ?
    '''

    user_data = await execute_query(query, [user_id], fetch='one')

    if user_data:
        return dict(zip(['user_id', 'date_last_msg'], user_data))


async def get_users():
    '''Возвращает список пользователей'''
    query = '''
    SELECT
        *
    FROM
        users
    '''

    users = await execute_query(query, fetch='all')

    return [dict(zip(['user_id', 'date_last_msg'], i)) for i in users]