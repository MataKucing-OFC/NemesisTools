import os, requests, time
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
import threading
import sys
from colorama import Fore, Style


def screen_clear():
    if os.name == "nt":
	    os.system("cls")
    else:
	    os.system("clear")


bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
res = Style.RESET_ALL
yl = Fore.YELLOW

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}

def laravelcheck (star):
    if "://" in star:
      star = star
    else:
      star = "http://" + star
    star = star.replace('\n', '').replace('\r', '')
    url = star + "/.env"
    check = requests.get(url, headers=headers, timeout=3)
    resp = check.text
    try:
        if "DB_HOST" in resp:
            print(f"Laravel {gr}OK{res} => {star}\n")
            mrigel = open("Results/Laravel.txt", "a")
            mrigel.write(f'{star}\n')
        else:
            print(f"{red}Not{res} Laravel => {star}\n")
    except:
        pass
def wpcheck (star):
    if "://" in star:
      star = star
    else:
      star = "http://" + star
    star = star.replace('\n', '').replace('\r', '')
    url = star + "/wp-content/"
    check = requests.get(url, headers=headers, timeout=3)
    try:
        if check.status_code == 200:
            print(f"Wordpress {gr}OK{res} => {star}\n")
            mrigel = open("Results/Wordpress.txt", "a")
            mrigel.write(f'{star}\n')
        else:
            print(f"{red}Not{res} Wordpress => {star}\n")
    except:
        pass


def filter(star):
    try:
       laravelcheck(star)
       wpcheck(star)
    except:
       pass


def main():
    print(f'''    
        __                                __   _       ______     ________  ________{wh}
       / /   ____ __{gr}_NEMESIS_{res} __   _____  / /  | |     / / __ \   / ____/  |/  / ___/{red}
      / /   / __ `/ ___/ __ `/ | / / _ \/ /   | | /| / / /_/ /  / /   / /|_/ /\__ \ {bl}
     / /___/ /_/ / /  / /_/ /| |/ /  __/ /    | |/ |/ / ____/  / /___/ /  / /___/ / {yl}
    /_____/\__,_/_/   \__,_/ |___/\___/_/     |__/|__/_/       \____/_/  /_//____/  {gr}
                                                        {wh}        GitHub : {red}MataKucing-OFC{res}                    
    ''')
    list = input(f"{gr}Give Me Your List.txt@{red}Nemesis> {gr}${res} ")
    star = open(list, 'r').readlines()
    try:
       ThreadPool = Pool(10)
       ThreadPool.map(filter, star)
       ThreadPool.close()
       ThreadPool.join()
    except:
       pass
       
if __name__ == '__main__':
    screen_clear()
    main()