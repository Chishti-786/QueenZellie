from pyrogram import Client, Filters

@Client.on_message(Filters.command(["boom"]))
async def start(client, message):
    boomtext = f"Hi"
    endtext = f"Complete boom"
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(boomtext)
    await message.reply_text(endtext)

