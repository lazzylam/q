import asyncio
from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import *

client = TelegramClient("lamora", API_ID, API_HASH)

async def main():
    await client.start(bot_token=BOT_TOKEN)
    register(client)
    print("aktif!")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())