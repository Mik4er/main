from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

from telegram import KeyboardButton, ReplyKeyboardMarkup, Message

TOKEN = "5304908817:AAGoCndOrT_BHXCnmxs_Q0bKJU-m5SZQe5U"
print("Bot is up")
updater = Updater(TOKEN)

def start_messege(update,context):
    chat = update.effective_chat
    buttons = [[KeyboardButton('English')], [KeyboardButton('Ukrainian')]]
    context.bot.send_message(chat_id=chat.id, text='🇺🇦 - Привіт! Обери свою мову: \n🇬🇧 - Hello! Chouse your language: ',
                             reply_markup = ReplyKeyboardMarkup(buttons))

def language(update,context):
    chat = update.effective_chat
    currency_code = update.message.text
    if currency_code in ("English"):
        buttons = [[KeyboardButton('Add new')], [KeyboardButton('Show all')]]
        context.bot.send_message(chat_id=chat.id,reply_markup = ReplyKeyboardMarkup(buttons),text = "hello!")
    if currency_code in ("Ukrainian"):
        buttons = [[KeyboardButton('Додати нову')], [KeyboardButton('Показати всі')]]
        context.bot.send_message(chat_id=chat.id,reply_markup = ReplyKeyboardMarkup(buttons),text = "привіт!")


def add_n(update,context):
    chat = update.effective_chat
    currency_code = update.message.text
    if currency_code in ("Add new"):
        message = "write something"
        context.bot.send_message(chat_id=chat.id, text=message)
    if currency_code in ("Додати нову"):
        message = 'напишіть щось'
        context.bot.send_message(chat_id=chat.id, text=message)   
    return 1


def show(update,context):
    chat = update.effective_chat
    currency_code = update.message.text
    if currency_code in ("Show all"):
        buttons = [[KeyboardButton('Delete')]]
        with open(f"{update.message.chat.id}.{update.message.chat.first_name}","r") as f:
            all_note = f.read()
        context.bot.send_message(chat_id=chat.id,reply_markup = ReplyKeyboardMarkup(buttons),text=all_note)
    if currency_code in ("Показати всі"):
        buttons = [[KeyboardButton('Видалити')]]
        with open(f"{update.message.chat.id}.{update.message.chat.first_name}","r") as f:
            all_note = f.read()
        context.bot.send_message(chat_id=chat.id,reply_markup = ReplyKeyboardMarkup(buttons),text=all_note)


def cancel(update,context):
    update.message.reply_text("Запис закінчено")
    return ConversationHandler.END


def saver(update,context):
    chat = update.effective_chat
    note = str(update.message.text)
    with open(f"{update.message.chat.id}.{update.message.chat.first_name}","a+") as f:
        f.write(note+"\n")
    context.bot.send_message(chat_id=chat.id, text="done")
    print("done")





add_new_hand = ConversationHandler(
    entry_points=[MessageHandler(Filters.text("Add new | Додати нову"),add_n)],
    states = {
        1: [MessageHandler(Filters.text & (~ Filters.command),saver)]
    },
    fallbacks=[CommandHandler("cancel",cancel)]
)



disp = updater.dispatcher
disp.add_handler(CommandHandler('start',start_messege))
# disp.add_handler(MessageHandler(Filters.regex("Add new"),add_n))
# disp.add_handler(MessageHandler(Filters.regex("Додати нову"),add_n))
disp.add_handler(MessageHandler(Filters.regex("Show all"),show))
disp.add_handler(MessageHandler(Filters.regex("Показати всі"),show))
disp.add_handler(add_new_hand)
disp.add_handler(MessageHandler(Filters.all,language))




updater.start_polling()
updater.idle()