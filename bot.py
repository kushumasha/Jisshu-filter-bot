import sys
import glob
import importlib
from pathlib import Path
from pyrogram import idle
import logging
import logging.config
from os import environ # <<-- এই লাইনটি যোগ করুন

# Get logging configurations
# logging.config.fileConfig("logging.conf") # <-- কমেন্ট আউট করুন
logging.getLogger().setLevel(logging.INFO)
# ... (বাকি logging কনফিগারেশন)

from pyrogram import __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import *
from utils import temp
from Script import script
from datetime import date, datetime
import pytz
from aiohttp import web
from plugins import web_server, check_expired_premium
import pyrogram.utils
import asyncio
from Jisshu.bot import JisshuBot
from Jisshu.util.keepalive import ping_server
from Jisshu.bot.clients import initialize_clients

ppath = "plugins/*.py"
files = glob.glob(ppath)
# JisshuBot.start() # <-- এখান থেকে লাইনটি মুছে ফেলুন
loop = asyncio.get_event_loop()

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647


async def Jisshu_start():
    print("\n")
    print("Credit - Telegram @JISSHU_BOTS")
    
    await JisshuBot.start() # <-- এখানে যোগ করুন
    
    bot_info = await JisshuBot.get_me()
    JisshuBot.username = bot_info.username
    await initialize_clients()
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"plugins/{plugin_name}.py")
            import_path = "plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["plugins." + plugin_name] = load
            print("JisshuBot Imported => " + plugin_name)

    # Heroku এবং Render উভয়ের জন্য keep-alive পিং
    if ON_HEROKU or environ.get("RENDER"):
        asyncio.create_task(ping_server())

    b_users, b_chats = await db.get_banned()
    temp.BANNED_USERS = b_users
    temp.BANNED_CHATS = b_chats
    await Media.ensure_indexes()
    me = await JisshuBot.get_me()
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    temp.B_LINK = me.mention
    JisshuBot.username = "@" + me.username
    JisshuBot.loop.create_task(check_expired_premium(JisshuBot))
    logging.info(
        f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}."
    )
    logging.info(script.LOGO)
    tz = pytz.timezone("Asia/Kolkata")
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S %p")
    
    # এই মেসেজগুলো পাঠাবার আগে নিশ্চিত করুন LOG_CHANNEL, SUPPORT_GROUP আইডি ঠিক আছে এবং বট ওই চ্যানেল/গ্রুপে অ্যাডমিন আছে
    try:
        await JisshuBot.send_message(
            chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(me.mention, today, time)
        )
        if SUPPORT_GROUP:
            await JisshuBot.send_message(
                chat_id=SUPPORT_GROUP, text=f"<b>{me.mention} ʀᴇsᴛᴀʀᴛᴇᴅ 🤖</b>"
            )
    except Exception as e:
        logging.warning(f"Unable to send restart message: {e}")

    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()
    await idle()


if __name__ == "__main__":
    try:
        loop.run_until_complete(Jisshu_start())
    except KeyboardInterrupt:
        logging.info("Service Stopped Bye 👋")
