import telebot
import requests
import time
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time

bot = telebot.TeleBot("1921476703:AAEvCq_uL0OW3xfd4SBHHERmOjIp7IxN7ds", parse_mode='HTML')

options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-sh-usage')


@bot.message_handler(commands=['cmd'])
def send_welcome(message):
		driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)
		driver.get('https://www.edatel.com.co/mi-ip')
		time.sleep(1)
		mymacs = driver.find_element_by_xpath('/html').text
		print(mymacs)
		bot.reply_to(message, mymacs)



try:
	bot.polling()

except:
	bot.polling()
