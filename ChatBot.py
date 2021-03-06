import logging
import random
import telegram
from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler, Updater

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

apiKeyFile = open("/home/yong/server/NSU_Meal_Bot_Telegram_KEY", 'r')
TOKEN = apiKeyFile.read().rstrip('\n')
apiKeyFile.close()

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, Wolrd!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

def sendMenuMessage(update, context):
    if ("1층" in update.message.text) and (("중식" in update.message.text) or ("점심" in update.message.text)):
        db = open("/home/pi/nsu_serverDB/hak1st_lunch", 'r')
        context.bot.send_message(chat_id=update.effective_chat.id, text=db.read())
        db.close()
    if ("1층" in update.message.text) and (("석식" in update.message.text) or ("저녁" in update.message.text)):
        db = open("/home/pi/nsu_serverDB/hak1st_dinner", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    if ("2층" in update.message.text) and (("중식" in update.message.text) or ("점심" in update.message.text)):
        db = open("/home/pi/nsu_serverDB/hak2nd_lunch", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    if ("2층" in update.message.text) and (("석식" in update.message.text) or ("저녁" in update.message.text)):
        db = open("/home/pi/nsu_serverDB/hak2nd_dinner", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    if ("채움" in update.message.text) and (("조식" in update.message.text) or ("아침" in update.message.text)):
        db = open("/home/pi/nsu_serverDB/chaeum_breakfast", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    if ("채움" in update.message.text) and (("중식" in update.message.text) or ("점심" in update.message.text)):
        db = open("/home/pi/nsu_serverDB/chaeum_lunch", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    if ("채움" in update.message.text) and (("석식" in update.message.text) or ("저녁" in update.message.text)):
        db = open("/home/pi/nsu_serverDB/chaeum_dinner", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()

message_handler = MessageHandler(Filters.text, sendMenuMessage)
dispatcher.add_handler(message_handler)