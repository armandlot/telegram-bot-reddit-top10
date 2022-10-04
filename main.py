from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram import Update
import config
import logging

updater = Updater(token=config.API_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def main():
    print("Hello world")
    if (config.API_TOKEN != ''):
        print("...I know something that you don't!")
    else :
        print("No api_token found, please create a config.py file, and save your api token as API_TOKEN.")
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bi-bup, I'm a bot.")

if __name__ == '__main__':
    main()
