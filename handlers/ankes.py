from telethon import events
from database import db

def register(client):
    @client.on(events.NewMessage)
    async def antigcast_handler(event):
        sender = await event.get_sender()
        if sender.bot or sender.id in db.whitelist_users:
            return

        message_text = event.raw_text.lower()
        if any(word in message_text for word in db.whitelist_words):
            return

        if ("t.me/" in message_text or
            "@" in message_text or
            any(word in message_text for word in db.blacklist_words) or
            sender.id in db.blacklist_users):
            try:
                await event.delete()
                print(f"Pesan dari {sender.id} dihapus.")
            except:
                pass
