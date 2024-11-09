import asyncio
import aiohttp

from config import TOKEN

URL = f"https://api.telegram.org/bot{TOKEN}/getMe"

async def main():
    offset = None
    async with aiohttp.ClientSession() as session:
        params = {'offset': offset, 'timeout': 10}
        while True:
            async with session.get(URL + 'getUpdates', data=params) as response:
                updates = await response.json()
                if len(updates['result']) > 0:
                    offset = updates['result'][-1]['update_id'] + 1
                    for update in updates['result']:

















