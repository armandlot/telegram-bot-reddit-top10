from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update
import config
import logging

updater = Updater(token=config.API_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def main():
    print("Bot started...")
    if (config.API_TOKEN != ''):
        print("...I know something that you don't!")
    else :
        print("No api_token found, please create a config.py file, and save your api token as API_TOKEN.")
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    #-- handlers definition --
    #- start command
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    #- top10 command
    top10_handler = CommandHandler('top10', top10)
    dispatcher.add_handler(top10_handler)
    #- echo response (no command)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)
    # start listening
    updater.start_polling()

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bi-bup, I'm a bot.\nType /top10 then a subreddit and I'll fetch the top10 posts for this sub.")

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def top10(update: Update, context: CallbackContext):
    reddit_sub = ' '.join(context.args)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Lemme fetch Top10 posts from: " + reddit_sub)

if __name__ == '__main__':
    main()
