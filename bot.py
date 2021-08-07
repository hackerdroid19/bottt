import requests
import datetime
import time
import indexBot
import gateAnubis
import re

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

token = '1907345065:AAEZf1TF-EhbSvl1rsHTY6vyh_WFoASrAIc'
magnito_bot = indexBot.BotHandler(token)

def main():
    new_offset = 0
    print('hi, now launching...')

    while True:
        all_updates=magnito_bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                #print(current_update)
                first_update_id = current_update['update_id']
                try:
	                if 'text' not in current_update['message']:
	                    first_chat_text='New member'
	                else:
	                    first_chat_text = current_update['message']['text']
	                first_chat_id = current_update['message']['chat']['id']
	                mid = current_update['message']['message_id']

	                if '/send' in first_chat_text:
	                	x = ''
	                	cccap = re.findall(r'\d+', first_chat_text)
	                	for ccadd in cccap:
	                		x=x+str(ccadd)
	                	validccn = x[0:1]
	                	valdyer = x[18:22]
	                	validlen = len(x)
	                	year= ['2021','2022','2023','2024','2025','2026','2027','2028','2029','2030','2031','2032','2033','2034','2035']

	                	if validccn == '4' or validccn =='5':
	                		if valdyer in year:
	                			if validlen >=25:
	                				magnito_bot.send_message(first_chat_id,'<b>⚜️ Gate Anubis ⚜️\n\n- Procesando Tu Solicitud.. ⏳\n\n🔱Bot by --» @Raulshp</b>')
		                			gateAnubis.start(x,first_chat_id,mid)
		                		else:
		                			magnito_bot.send_message(first_chat_id,'<b>⚜️ Gate Anubis ⚜️\n\n- ⚠️ Number is invalid\n\n🔱Bot by --» @Raulshp</b>')
		                	else:
		                		magnito_bot.send_message(first_chat_id,'<b>⚜️ Gate Anubis ⚜️\n\n- ⚠️ Año debe ser 20xx\n\n🔱Bot by --» @Raulshp</b>')
		                else:
		                	magnito_bot.send_message(first_chat_id,'<b>⚜️ Gate Anubis ⚜️\n\n- ⚠️ Number is invalid\n\n🔱Bot by --» @Raulshp</b>')
	                	new_offset = first_update_id + 1                	
                	pass
                except:
                	print('hi')




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
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