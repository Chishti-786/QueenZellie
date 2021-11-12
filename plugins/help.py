#Copyrigt (C) 2021 SinhalayaCreator

 #
 #░░░▄▀▄░█░█░█▀▀░█▀▀░█▀█░░
 #░░░█\█░█░█░█▀▀░█▀▀░█░█░░
 #░░░░▀\░▀▀▀░▀▀▀░▀▀▀░▀░▀░░
 #░▀▀█░█▀▀░█░░░█░░░▀█▀░█▀▀
 #░▄▀░░█▀▀░█░░░█░░░░█░░█▀▀
 #░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀
 #POWERED BY A.N.TECH CREW


from pyrogram import Client, Filters


@Client.on_message(Filters.command(["panel"]))
async def start(client, message):
    panneltxt = f"Queen Zellie Command List"
    await message.reply_text(panneltxt)
    
    
