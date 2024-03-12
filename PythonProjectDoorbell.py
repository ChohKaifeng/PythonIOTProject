import RPi.GPIO as GPIO
import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from picamera import PiCamera

# Set Path
path=os.getenv('HOME/pi/')

# Set Telegram bot 
bot = telebot.TeleBot("", parse_mode=None) # Add in Telegrambot ID
markup = InlineKeyboardMarkup()
markup.row_width = 2
markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"), InlineKeyboardButton("No", callback_data="cb_no"))

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22, GPIO.OUT) # Switch
GPIO.setup(17,GPIO.IN) # set PIR (Motion Sensor)

closeToDoor = False

# Function to take picture
def take_picture():
    my_camera = PiCamera();
    my_camera.resolution=(1920,1080);
    my_camera.vflip=True;
    my_camera.hflip=True;
    my_camera.capture('/home/pi/image.jpg')
    my_camera.close()

# Function to send picture & message
def telegram_bot(inputData):
    photo = open('/home/pi/image.jpg', 'rb')
    bot.send_photo(___telegram account, photo) # REPLACE ___telegram account WITH YOUR TELEGRAM ACCOUNT KEY #
        
    if inputData == "doorbell":
        bot.send_message(___telegram account, "Hi " + "User" + "!\nThere is someone at the door now! Do you want to open the door? ", reply_markup=markup)# REPLACE ___telegram account WITH YOUR TELEGRAM ACCOUNT KEY #
    elif inputData == "sensor":
        bot.send_message(___telegram account, "Hi " + "User" + "!\nThere is someone standing too close to your door!")# REPLACE ___telegram account WITH YOUR TELEGRAM ACCOUNT KEY #

while(True):
    #This is the code if switch is on
    if GPIO.input(22):        
        print("Doorbell is pressed: " + str(GPIO.input(22)));

        # Call function to take image
        take_picture();
        #Code to send the image
        telegram_bot("doorbell")

    elif GPIO.input(17) == False:
        #Code for Camera to take picture if sensor detects someone
        take_picture();
        #Code to send the image
        telegram_bot("sensor")