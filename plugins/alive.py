import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3eaa696690c2910facd2a.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━
✨ ʜᴇʟʟᴏ, ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ᴀɴᴅ ɴᴏ ʟᴀɢ ɪssᴜᴇ ᴡɪᴛʜ ʙᴇsᴛ sᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ sᴏᴄɪᴀʟ ᴍᴇᴄʜᴀɴɪᴄ...
💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ [sᴏᴄɪᴀʟ ᴍᴇᴄʜᴀɴɪᴄ](https://t.me/Social_mechanic_1997)...
━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/SOCIAL_MECHANIC_MUSIC_BOT?startgroup=true")
        ],
        [
            InlineKeyboardButton("📝 ᴄᴏᴍᴍᴀɴᴅs", url="https://telegra.ph/ANGEL-VC-MUSIC-BOT-05-22"),
            InlineKeyboardButton("⚕️ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/social_mechanic_1997")
        ],
        [
            InlineKeyboardButton("👥 ᴏғғɪᴄɪᴀʟ ɢʀᴏᴜᴘ", url="https://t.me/tamil_chat_group_1"),
            InlineKeyboardButton("📣 ᴏғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ", url="https://t.me/social_mechanic")
        ],
        [
            InlineKeyboardButton("💠 ʏᴏᴜᴛᴜʙᴇ 💠", url="https://youtube.com/channel/UCRcRXNwpjSfobVWOhkbcSrQ")
        ]
   
     ]
  ),
)
    
    
@Client.on_message(commandpro(["/start", "/alive", "Social", "/repo"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3eaa696690c2910facd2a.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
             [
            [
                InlineKeyboardButton(text="👥 ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/tamil_chat_group_1"),
                InlineKeyboardButton(text="📣 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/social_mechanic"),
            ]
        ]
     ),
  ) 


@Client.on_message(commandpro(["/updates", "Channel"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3eaa696690c2910facd2a.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴊᴏɪɴ ᴛʜᴇsᴇ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ", url=f"https://youtube.com/channel/UCRcRXNwpjSfobVWOhkbcSrQ")
                ]
            ]
        ),
    )
