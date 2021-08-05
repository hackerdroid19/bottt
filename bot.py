import telebot
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

import time

bot = telebot.TeleBot("1921476703:AAEvCq_uL0OW3xfd4SBHHERmOjIp7IxN7ds", parse_mode='HTML')

@bot.message_handler(commands=['cmd'])
def send_welcome(message):
	def reload():
		try:
			bot.reply_to(message, "/ccgen \n /c")
		except:
			reload()
	reload()



try:
	bot.polling()

except:
	bot.polling()