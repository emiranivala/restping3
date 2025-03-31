from pyrogram import filters
from crushe import app
from crushe.core import script
from crushe.core.func import subscribe
from config import OWNER_ID
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# ------------------- Start-Buttons ------------------- #

buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url="https://t.me/+3bMBj190KOc3YzNk")],
        [InlineKeyboardButton("ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ", url="https://t.me/She_who_remain")]
    ]
)

@app.on_message(filters.command("start"))
async def start(_, message):
    join = await subscribe(_, message)
    if join == 1:
        return
    await message.reply_photo(photo="https://graph.org/file/a06275c5b4e838e2df0e5-664ae5f4d543dfd30d.jpg",
                              caption=script.START_TXT.format(message.from_user.mention), 
                              reply_markup=buttons)
