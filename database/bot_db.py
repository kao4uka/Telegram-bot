import random
import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print('База данных подлючена!')

    db.execute("CREATE TABLE IF NOT EXISTS mentors "
               "(id INTEGER PRIMARY KEY,"
               "name TEXT,"
               "age INTEGER,"
               "direction TEXT,"
               "groupe TEXT)")
    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors VALUES "
                       "(?, ?, ?, ?, ?)", tuple(data.values()))

        db.commit()

async def sql_command_random():
    result = cursor.execute("SELECT * FROM mentors").fetchall()
    random_mentor = random.choice(result)
    return random_mentor


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (user_id,))
    db.commit()


sql_create()