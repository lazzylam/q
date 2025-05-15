import asyncio
from telethon import TelegramClient
from config import api_id, api_hash, bot_token
from handlers import antigcast, commands

client = TelegramClient("lamora", api_id, api_hash)

async def main():
    await client.start(bot_token=bot_token)
    ankes.register(client)
    com.register(client)
    print("aktif!")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
