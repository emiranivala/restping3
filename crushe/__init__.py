#crushe

import asyncio
import logging
from pyromod import listen
from pyrogram import Client
from pyrogram.enums import ParseMode
from config import API_ID, API_HASH, BOT_TOKEN
from telethon.sync import TelegramClient


loop = asyncio.get_event_loop()

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)

# Filter out the empty messages warnings from Pyrogram
pyrogram_logger = logging.getLogger("pyrogram.types.messages_and_media.message")
pyrogram_logger.setLevel(logging.ERROR)

# Filter out connection and session logs from Pyrogram
logging.getLogger("pyrogram.session.auth").setLevel(logging.ERROR)
logging.getLogger("pyrogram.connection.connection").setLevel(logging.ERROR)
logging.getLogger("pyrogram.session.session").setLevel(logging.ERROR)
logging.getLogger("pyrogram.connection.transport.tcp.tcp").setLevel(logging.ERROR)
logging.getLogger("pyrogram.dispatcher").setLevel(logging.WARNING)
logging.getLogger("pyrogram.network.mtproto.mtproto_sender").setLevel(logging.ERROR)

# Filter out telethon logs
logging.getLogger("telethon").setLevel(logging.WARNING)

sex = TelegramClient('sexrepo', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

app = Client(
    "RestrictBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=10,
    sleep_threshold=20,
    max_concurrent_transmissions=5,
    parse_mode=ParseMode.HTML,
    workdir="."
)

async def restrict_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    await app.start()
    from pyrogram.types import BotCommand
    await app.set_bot_commands([
        BotCommand("start", "Launch the application"),
        BotCommand("batch", "Download in bulk"),
        BotCommand("login", "Login process to userbot"),
        BotCommand("logout", "Logout and clear data"),
        BotCommand("myplan", "View your personalized plan"),
        BotCommand("stats", "Display statistics and insights")
    ])
    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name


loop.run_until_complete(restrict_bot())


