from colorama import Fore, Style, Back
import os

bl = Fore.BLACK
wh = Fore.WHITE
yl = Fore.YELLOW
red = Fore.RED
res = Style.RESET_ALL
gr = Fore.GREEN
ble = Fore.BLUE
#NEMESIS 2019-2024
def screen_clear():
    if os.name == "nt":
	    os.system("cls")
    else:
	    os.system("clear")

screen_clear()


print(f'''
                   `\-.   `
                      \ `.  `
                       \  \ |
              __.._    |   \.       -
       ..---~~     ~ . |    Y
         ~-.          `|    |
            `.               `~~--.
              \                    ~.
               \                     \__. . -- -  .
         .-~~~~~      ,    ,            ~~~~~~---...._
      .-~___        ,'/  ,'/ ,'\          __...---~~~
            ~-.    /._\_( ,(/_. 7,-.    ~~---...__
           _...>-  P""6=`_/"6"~   6)    ___...--~~~
            ~~--._ \`--') `---'   9'  _..--~~~
                  ~\ ~~/_  ~~~   /`-.--~~
                    `.  ---    .'   \_
                      `. " _.-'     | ~-.,-------._
                  ..._../~~   ./       .-'    .-~~~-.
            ,--~~~ ,'...\` _./.----~~.'/    /'       `-
        _.-(      |\    `/~ _____..-' /    /      _.-~~`.
       /   |     /. ^---~~~~       ' /    /     ,'  ~.   
      (    /    (  .           _ ' /'    /    ,/      \   )
      (`. |     `\   - - - - ~   /'      (   /         .  |
       \.\|       \            /'        \  |`.           /
       /.'      `\         /'           ~-\         .  /
      /,   (        `\     /'                `.___..-      
     | |    \         `\_/'                  //      \.     |
     | |     |                 _NEMESIS_      /' |       |     |
    _   __                         _     ______            __    
  {red} / | / /__  ____ ___  ___  _____(_)___/_  __/___  ____  / /____
 {gr} /  |/ / _ \/ __ `__ \/ _ \/ ___/ / ___// / / __ \/ __ \/ / ___/
 {yl}/ /|  /  __/ / / / / /  __(__  ) (__  )/ / / /_/ / /_/ / (__  ) 
/_/ |_/\___/_/ /_/ /_/\___/____/_/____//_/  \____/\____/_/____/{res}
                             {gr}Nemesis{res} {ble}Free Tools{res}, {red}GitHub : MataKucing-OFC{res}
{red}WARNING!{wh} Selling these tools for personal gain is strictly prohibited!   
{red}PERHATIAN!{wh} Dilarang keras memperjual belikan tools ini untuk kepentingan pribadi
                {gr}This Is Free Tools!                         
{yl}---------------- SPAMMING ------------------                                          
{red}[{yl}1{red}]:{res} Mass Grabber Valid All SMTPs , Twilio, Aws Keys, Nexmo, MySql {red} HOT!!
{red}[{yl}2{red}]:{res} Mass Aws Keys Quota Checker ++ Auto Root Aws Console (Admin Dashboard (RDPs,VPS, SES ...)) {red} HOT!!
{red}[{yl}3{red}]:{res} Mass SMTPs Checker
{red}[{yl}4{red}]:{res} Mass Sendgrid Api Checker
{red}[{yl}5{red}]:{res} Mass Twilio Checker
{red}[{yl}6{red}]:{res} Mass Nexmo Balance Checker
{yl}---------------- HACKING -------------------                                   
{red}[{yl}7{red}]:{res} Zone-H Grabber                                               
{red}[{yl}8{red}]:{res} Bing Dorker  {red} HOT!!
{red}[{yl}9{red}]:{res} Mass Reverse Domains => IPs 
{red}[{yl}10{red}]:{res} Mass IPS Ranger 
{red}[{yl}11{red}]:{res} Mass Laravel, Wordpress Filter {yl} NEW!!
{red}[{yl}12{red}]:{res} MASS BYPASS & UPLOAD SHELL (LARAVEL) {red} HOT!!
{red}[{yl}13{red}]:{res} Website Auto Exploit & Upload Shell!  {red} HOT!! {yl} NEW!!
{red}[{yl}14{red}]:{res} Find Path KcFinder {yl} NEW!!
{yl}---------------- NEXT UPDATE : -------------------
{red}Mass Symlink Shells
Mass Create Smtp From Shells
Mass Extract Emails From Shells
Mass Upload Mailers From Shells
Mass Check Working Shells
Mass Cp Rest From Shells
Mass Mail Check From Shells
Mass Find Access Hash From Shells
Mass Find Cpanel  From Shells
Mass File Upload From Shells [Random]
Mass Symlink & Brute Force Cpanel From Shells
Mass Wordpress Pass Change From Shells
Mass Shell Upload In Wordpress Panel
Shell Replacement  T-Shop/Olux/Xleet
Mass Cpanel Checker
Mass Cpanel Upload File
Mass Email Bounced Checker
Mass Smtp Checker
Mass Grab Sites ViewDns/HackTarget
Mass SpyMailer Sender{res}
{red}[{yl}15{red}]:{res} Check Update
''')

choice = input(f'{gr}Give Me Your Choice{wh}/{red}> {gr}${res} ')
if choice == '1':
    
    link = input(f'{gr}Give Me Your List.txt{wh}/{red} > {gr}${res} ')
    os.system(f'python3 Scripts/grabber.py {link}')
if choice == '2':
    
    os.system('python3 Scripts/aws2.py')
if choice == '3':
    
    os.system('python3 Scripts/checker.py')
if choice == '4':
    
    os.system('python3 Scripts/sendg.py')
if choice == '5':
    
    os.system('python3 Scripts/api.py')
if choice == '6':
    
    os.system('python3 Scripts/nexmo.py')
if choice == '7':
    os.system('python3 Scripts/zone.py')
if choice == '8':
    
    os.system('python3 Scripts/scanner.py')
if choice == '9':
    
    os.system('python3 Scripts/ipfromdomain.py')
if choice == '10':
    
    os.system('perl Scripts/ranger.pl')
if choice == '11':
    
    os.system('python3 Scripts/laravelcms.py')
if choice == '12':
    
    os.system('python3 Scripts/up.py')
if choice == '13':
    os.chdir("Scripts/auto")
    os.system('python2 latest.py')
if choice == '14':
    os.chdir("Scripts/finP")
    os.system('python3 find.py')
if choice == '15':
    print("Check Update From GitHub : MataKucing-OFC")