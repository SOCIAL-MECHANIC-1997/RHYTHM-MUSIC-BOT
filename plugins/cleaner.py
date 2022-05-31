# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 (C) 2022 𝑩𝒚 @𝑨𝒅𝒊𝒕𝒚𝒂𝑯𝒂𝒍𝒅𝒆𝒓

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from modules.helpers.filters import command, other_filters
from modules.helpers.decorators import sudo_users_only, errors

downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(command(["rmd", "clear"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **𝑫𝒆𝒍𝒆𝒕𝒆𝒅 𝑨𝒍𝒍 𝑫𝒐𝒘𝒏𝒍𝒐𝒂𝒅𝒆𝒅 𝑭𝒊𝒍𝒆𝒔 ...**")
    else:
        await message.reply_text("❌ **𝑵𝒐 𝑭𝒊𝒍𝒆𝒔 𝑫𝒐𝒘𝒏𝒍𝒐𝒂𝒅𝒆𝒅 ...**")

        
@Client.on_message(command(["rmr", "clean"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw_files)
    if ls_dir:
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("✅ **𝑫𝒆𝒍𝒆𝒕𝒆𝒅 𝑨𝒍𝒍 𝑹𝒂𝒘 𝑭𝒊𝒍𝒆𝒔 ...**")
    else:
        await message.reply_text("❌ **𝑵𝒐 𝑹𝒂𝒘 𝑭𝒊𝒍𝒆𝒔 𝒊𝒏 𝑺𝒆𝒓𝒗𝒆𝒓 ...**")


@Client.on_message(command(["cleanup"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("✅ **𝑪𝒍𝒆𝒂𝒏𝒆𝒅 𝑨𝒍𝒍 𝑱𝒖𝒏𝒌𝒔 𝑻𝒉𝒖𝒎𝒏𝒂𝒊𝒍𝒔 ...**")
    else:
        await message.reply_text("✅ **𝑨𝒍𝒓𝒆𝒂𝒅𝒚 𝑪𝒍𝒆𝒂𝒏𝒆𝒅 𝑨𝒍𝒍 𝑱𝒖𝒏𝒌𝒔 ...**")
