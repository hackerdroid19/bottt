import telebot
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

import time

bot = telebot.TeleBot("1921476703:AAEvCq_uL0OW3xfd4SBHHERmOjIp7IxN7ds", parse_mode='HTML')

options = webdriver.ChromeOptions()
options.add_argument("window-size=1200x1000")
options.add_argument("--log-level=3")
options.add_argument("--disable-extensions");
options.add_argument("test-type");
#options.add_argument('headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-single-click-autofill");
options.add_argument("--disable-autofill-keyboard-accessory-view[8]");
options.add_experimental_option('excludeSwitches', ['enable-logging'])

@bot.message_handler(commands=['cmd'])
def send_welcome(message):
		driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)
		driver.get('https://steerable-pail.000webhostapp.com/page/macs.html')
		time.sleep(1)
		mymacs = driver.find_element_by_xpath('/html').text
		print(mymacs)
		bot.reply_to(message, mymacs)



try:
	bot.polling()

except:
	bot.polling()