"""


import asyncpg

from config import DB_DSN

async def connect_db():
    return await asyncpg.connect(
        user='gen_user',
        password='1234567890a',
        database='default_db',
        host='103.88.242.89',
        port=5432
    )


async def save_interest(interest: str, username: str):
    conn = await asyncpg.connect(DB_DSN)
    await conn.execute("INSERT INTO AIbotTable (interest, username) VALUES ($1, $2)", interest, username)
    await conn.close()
"""
