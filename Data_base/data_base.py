import sqlite3

conn = sqlite3.connect('Data base/database.db')
curs = conn.cursor()


async def db_start():
    curs.execute("CREATE TABLE IF NOT EXISTS Users ("
                 "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                 "username TEXT, "
                 "interests TEXT, "
                 "channel TEXT)")
    conn.commit()
    curs.close()
    conn.close()
