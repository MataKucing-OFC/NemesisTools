from colorama import Fore, Style
import os, vonage
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
 _   _                             ____        _                         _____ _               _             {wh}
| \ | |                           |  _ \      | |                       / ____| |             | |            {red}
|  \| | ____{red}NEMESIS_{res}  ____   ___   | |_) | __ _| | __ _ _ __   ___ ___  | |    | |__   ___  ___| | _____ _ __{ble} 
| . ` |/ _ \ \/ / '_ ` _ \ / _ \  |  _ < / _` | |/ _` | '_ \ / __/ _ \ | |    | '_ \ / _ \/ __| |/ / _ \ '__|{yl}
| |\  |  __/>  <| | | | | | (_) | | |_) | (_| | | (_| | | | |{red} (_|  __/ | |____| | | |  __/ (__|   <  __/ |   {wh}
{gr}|_| \_|\___/_/\_\_| |_| |_|\___/  |____/ \__,_|_|\__,_|_| |_|\___\___|  \_____|_| |_|\___|\___|_|\_\___|_|{gr}
              {gr}                                                   {wh}   GitHub : {red}MataKucing-OFC{res}
''')
link = input(f"\n{gr}Give Me Nexmo_List.txt@{red}Nemesis>{gr} ${res} ")
with open(link) as fp:
    for star in fp:
        try:
            check = star.rstrip()
            ch = check.split('\n')[0].split('|')
            Key = ch[0]
            Sec = ch[1]
            client = vonage.Client(key=Key, secret=Sec)
            result = client.get_balance()
            print(f"{yl} {Key}|{Sec} {gr} Working API!{ble} Balance : {result['value']:0.2f} EUR{res}")
            open("Results/!Valid_Api.txt", "a").write(f"{Key}|{Sec} Balance: {result['value']:0.2f} EUR\n")
        except:
            print(f"{yl} {Key}|{Sec}  {red}DEAD API!{res}\n")
            pass
