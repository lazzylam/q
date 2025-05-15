import asyncio
from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import antigcast, commands

client = TelegramClient("lamora", API_ID, API_HASH)

async def main():
    await client.start(BOT_TOKEN=BOT_TOKEN)
    ankes.register(client)
    com.register(client)
    print("aktif!")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
