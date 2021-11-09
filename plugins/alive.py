from pyrogram import Client, Filters

@Client.on_message(Filters.command(["alive"]))
async def start(client, message):
    alivemsg = f"Queen Zellie is online now"
    await message.reply_text(alivemsg)