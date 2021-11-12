#Copyrigt (C) 2021 SinhalayaCreator

 #
 #░░░▄▀▄░█░█░█▀▀░█▀▀░█▀█░░
 #░░░█\█░█░█░█▀▀░█▀▀░█░█░░
 #░░░░▀\░▀▀▀░▀▀▀░▀▀▀░▀░▀░░
 #░▀▀█░█▀▀░█░░░█░░░▀█▀░█▀▀
 #░▄▀░░█▀▀░█░░░█░░░░█░░█▀▀
 #░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀
 #POWERED BY A.N.TECH CREW


from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/antechcrew")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/sasmithaaaaa")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/panel for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
