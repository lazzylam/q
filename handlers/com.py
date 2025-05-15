import asyncio
from telethon import events
from database import db, save_db

def register(client):
    @client.on(events.NewMessage(pattern="/addbl"))
    async def add_blacklist_user(event):
        reply = await event.get_reply_message()
        if reply:
            uid = reply.sender_id
        else:
            try:
                uid = int(event.raw_text.split(" ", 1)[1])
            except:
                msg = await event.reply("Format salah. Gunakan /addbl <user_id> atau reply.")
                await asyncio.sleep(2)
                await msg.delete()
                return
        if uid not in db.blacklist_users:
            db.blacklist_users.append(uid)
            save_db()
            msg = await event.reply(f"User `{uid}` ditambahkan ke blacklist.")
            await asyncio.sleep(2)
            await msg.delete()

    @client.on(events.NewMessage(pattern="/addwhite"))
    async def add_whitelist_user(event):
        reply = await event.get_reply_message()
        if reply:
            uid = reply.sender_id
        else:
            try:
                uid = int(event.raw_text.split(" ", 1)[1])
            except:
                msg = await event.reply("Format salah. Gunakan /addwhite <user_id> atau reply.")
                await asyncio.sleep(2)
                await msg.delete()
                return
        if uid not in db.whitelist_users:
            db.whitelist_users.append(uid)
            save_db()
            msg = await event.reply(f"User `{uid}` ditambahkan ke whitelist.")
            await asyncio.sleep(2)
            await msg.delete()

    @client.on(events.NewMessage(pattern="/bl"))
    async def add_blacklist_word(event):
        reply = await event.get_reply_message()
        if reply:
            word = reply.raw_text
        else:
            try:
                word = event.raw_text.split(" ", 1)[1]
            except:
                msg = await event.reply("Format salah. Gunakan /bl <kata> atau reply.")
                await asyncio.sleep(2)
                await msg.delete()
                return
        if word not in db.blacklist_words:
            db.blacklist_words.append(word)
            save_db()
            msg = await event.reply(f"Kata `{word}` ditambahkan ke blacklist.")
            await asyncio.sleep(2)
            await msg.delete()

    @client.on(events.NewMessage(pattern="/white"))
    async def add_whitelist_word(event):
        reply = await event.get_reply_message()
        if reply:
            word = reply.raw_text
        else:
            try:
                word = event.raw_text.split(" ", 1)[1]
            except:
                msg = await event.reply("Format salah. Gunakan /white <kata> atau reply.")
                await asyncio.sleep(2)
                await msg.delete()
                return
        if word not in db.whitelist_words:
            db.whitelist_words.append(word)
            save_db()
            msg = await event.reply(f"Kata `{word}` ditambahkan ke whitelist.")
            await asyncio.sleep(2)
            await msg.delete()

    @client.on(events.NewMessage(pattern="/listbl"))
    async def list_blacklist(event):
        users = "\n".join(str(u) for u in db.blacklist_users) or "Kosong"
        words = "\n".join(db.blacklist_words) or "Kosong"
        msg = await event.reply(f"**Blacklist Users:**\n{users}\n\n**Blacklist Words:**\n{words}")
        await asyncio.sleep(2)
        await msg.delete()

    @client.on(events.NewMessage(pattern="/listwhite"))
    async def list_whitelist(event):
        users = "\n".join(str(u) for u in db.whitelist_users) or "Kosong"
        words = "\n".join(db.whitelist_words) or "Kosong"
        msg = await event.reply(f"**Whitelist Users:**\n{users}\n\n**Whitelist Words:**\n{words}")
        await asyncio.sleep(2)
        await msg.delete()