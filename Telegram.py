import RPi.GPIO as GPIO
from time import sleep;
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("", parse_mode=None) # Add in Telegrambot ID

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24, GPIO.OUT) # LED
GPIO.setup(18, GPIO.OUT) # buzzer

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    user_name = message.from_user.username
    bot.send_message(chat_id, "Hi " + user_name + "!\nWelcome to your new doorbell!")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        GPIO.output(24,1)
    elif call.data == "cb_no":
        GPIO.output(18,1) # Buzzer turns on
        sleep(0.5)
        GPIO.output(18,0) # Buzzer turns off
    
    # Off the lights after 3 seconds
    sleep(3)
    GPIO.output(24,0) # LED turn off

bot.infinity_polling()