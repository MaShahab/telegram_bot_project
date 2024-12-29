from telegram import Update, MessageEntity, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler

async def salam_function(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(text='سلام \n به ربات تلگرام شهاب الدین خوش آمدید', chat_id=update.message.from_user.id)

async def user_info(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(update.message)
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    user_name = update.message.chat.username
    user_id = update.message.chat.id
    date_time = update.message.date
    await context.bot.send_message(text=f'User_id: {user_id} \n Name: {first_name}  {last_name} \n UserName: @{user_name} \n DateTime: {date_time}', chat_id=update.message.from_user.id)

async def echo_message(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(text="salam", chat_id=update.message.from_user.id)

async def delete_message(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.delete_message(chat_id=update.message.chat.id, message_id= update.message.message_id)

async def message_link_detection(update:Update, context:ContextTypes.DEFAULT_TYPE):
    links = [MessageEntity.URL]

    if update.message.parse_entities(types=links):
        await context.bot.send_message(chat_id=update.message.chat.id, text="اخطار: شما بر خلاف قوانین گروه، لینک ارسال کرده اید.")
        await context.bot.delete_message(chat_id=update.message.chat.id, message_id= update.message.message_id)


async def linksCommand(update:Update, context:ContextTypes.DEFAULT_TYPE):

    key = [['website'],['telegram','instagram']]
    key_2 = ReplyKeyboardMarkup(key)
    await context.bot.send_message(chat_id=update.message.chat.id, text="برای ارتباط با ما از طرق زیر میتوانید در شبکه های اجتماعی با ما ارتباط برقرار کنید.", reply_markup=key_2)

    

async def links(update:Update, context:ContextTypes.DEFAULT_TYPE):
    
    if update.message.text == "telegram":
        await context.bot.send_message(chat_id=update.message.chat.id, text="telegram_link")
    elif update.message.text == "instagram":
        await context.bot.send_message(chat_id=update.message.chat.id, text="instagram_link")
    elif update.message.text == "website":
        await context.bot.send_message(chat_id=update.message.chat.id, text="website_link")
    


async def show_inline_buttons(update:Update, context:ContextTypes.DEFAULT_TYPE):
    buttons = [[InlineKeyboardButton(text="web site", callback_data='Web')],[InlineKeyboardButton(text="My telegram account", callback_data='Tel'), InlineKeyboardButton(text="My instagram account", callback_data='Insta')]]
    key = InlineKeyboardMarkup(buttons)
    await context.bot.send_message(chat_id=update.message.chat.id, text="لطفا انتخاب کنید", reply_markup=key)

async def inline_handler_function(update:Update, context:ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    print(query.data)




if __name__ == "__main__":
    application = ApplicationBuilder().token("6686947229:AAFAcURQ1skvDR6UmoCHF3vXv9x8VOSxYhM").build()
    start_handler = CommandHandler('salam', salam_function)
    user_info_handler = CommandHandler('user_info', user_info)
    links_commadn_handler = CommandHandler('links', linksCommand)
    show_inline_buttons_handler = CommandHandler('show_inlines', show_inline_buttons)
    inline_handle = CallbackQueryHandler(inline_handler_function)
    echo_message_handler = MessageHandler(filters.TEXT, echo_message)
    delete_message_handler = MessageHandler(filters.ALL, delete_message)
    link_detection_henadler = MessageHandler(filters.ALL, message_link_detection)
    links_handler = MessageHandler(filters.ALL, links)
    # application.add_handler(start_handler)
    # application.add_handler(user_info_handler)
    # application.add_handler(delete_message_handler)
    # application.add_handler(echo_message_handler)
    # application.add_handler(link_detection_henadler)
    application.add_handler(show_inline_buttons_handler)
    application.add_handler(inline_handle)
    application.add_handler(links_handler)
    application.run_polling()