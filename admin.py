from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler

async def start_function(update:Update, context:ContextTypes.DEFAULT_TYPE):

    if update.message.chat.id != 158268525:
        user_name = update.message.chat.username
        user_id = update.message.chat.id
        await context.bot.send_message(text=f' کاربر جدیدی با مشخصات کاربری زیر ربات را استارت کرد. \n  UserName: @{user_name} \n User_id: {user_id}', chat_id=158268525)
    
    
    

if __name__ == "__main__":
    application = ApplicationBuilder().token("6686947229:AAFAcURQ1skvDR6UmoCHF3vXv9x8VOSxYhM").build()
    start_handler = CommandHandler('start', start_function)
    application.add_handler(start_handler)
    application.run_polling()
