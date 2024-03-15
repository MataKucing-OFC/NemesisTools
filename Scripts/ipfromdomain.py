import sys,os,re,socket,binascii,time,json,random,threading,pprint,smtplib,telnetlib,os.path,hashlib,string,glob,sqlite3,argparse,marshal,base64,colorama,requests
from random import choice
from colorama import Fore,Back,init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from time import strftime
from colorama import Fore,init, Style

def screen_clear():
    if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
bl = Fore.BLACK
wh = Fore.WHITE
yl = Fore.YELLOW
red = Fore.RED
res = Style.RESET_ALL
gr = Fore.GREEN
ble = Fore.BLUE

screen_clear()
print(f'''
    ____         ____                        ____                        _     {wh}
   /  _/___     / __/______{gr}NEMESIS{res}__ ___     / __ \____  ____ ___  ____ _(_)___ {red}
   / // __ \   / /_/ ___/ __ \/ __ `__ \   / / / / __ \/ __ `__ \/ __ `/ / __ \{ble}
 _/ // /_/ /  / __/ /  / /_/ / / / / / /  / /_/ / /_/ / / / / / / /_/ / / / / /{yl}
/___/ .___/  /_/ /_/   \____/_/ /_/ /_/  /_____/\____/_/ /_/ /_/\__,_/_/_/ /_/ {gr}
   /_/                                                      {wh} GitHub : {red}MataKucing-OFC{res}
''')

def getIP(site):
	
		site = i.strip()
		try:
			if 'http://' not in site:
				IP1 = socket.gethostbyname(site)
				print ("IP: "+IP1)
				open('ips.txt', 'a').write(IP1+'\n')
			elif 'http://' in site:
				url = site.replace('http://', '').replace('https://', '').replace('/', '')
				IP2 = socket.gethostbyname(url)
				print ("IP: "+IP2)
				open('ips.txt', 'a').write(IP2+'\n')
	
		except:
			pass
			
nam=input(f"{gr}Give Me Your Domain@{red}Nemesis> {gr}${res} ")
with open(nam) as f:
    for i in f:
        getIP(i)

		
