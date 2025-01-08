from colorama import Fore, Style, Back
import os
import random
from prettytable import PrettyTable
bl = Fore.BLACK
wh = Fore.WHITE
yl = Fore.YELLOW
red = Fore.RED
res = Style.RESET_ALL
gr = Fore.GREEN
ble = Fore.BLUE
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[0m'
    red = Fore.RED
#NEMESIS 2019-2025
def screen_clear():
    if os.name == "nt":
	    os.system("cls")
    else:
	    os.system("clear")

screen_clear()
logo = (f'''
    _   __                         _     ______            __    
  {red} / | / /__  ____ ___  ___  _____(_)___/_  __/___  ____  / /____
 {gr} /  |/ / _ \/ __ `__ \/ _ \/ ___/ / ___// / / __ \/ __ \/ / ___/
 {yl}/ /|  /  __/ / / / / /  __(__  ) (__  )/ / / /_/ / /_/ / (__  ) 
/_/ |_/\___/_/ /_/ /_/\___/____/_/____//_/  \____/\____/_/____/{res}
{gr}Nemesis{res} {ble}Free Tools{res}, {red}GitHub : MataKucing-OFC{res}
{red}WARNING!{wh} Selling these tools for personal gain is strictly prohibited!   
{red}PERHATIAN!{wh} Dilarang keras memperjual belikan tools ini untuk kepentingan pribadi
{gr}This Is Free Tools!                         
{res}
\033[94mVERSION        : \033[93m1.8 NemesisTools
\033[94mGITHUB       : \033[93mMataKucing-OFC                   

''')
banner = (f'''


\033[1;32;40m[----------SPAMMING----------]

 \033[91m[1] Mass Grabber Valid All SMTPs, Twilio, Aws Keys, Nexmo, MySql HOT!!                                                 
 \033[92m[2] Mass Aws Keys Quota Checker ++ Auto Root Aws Console (Admin Dashboard (RDPs,VPS, SES ...)) HOT!!        
 \033[93m[3] Mass SMTPs Checker        
 \033[94m[4] Mass Sendgrid Api Checker                              
 \033[95m[5] Mass Twilio Checker                                              
 \033[96m[6] Mass Nexmo Balance Checker

\033[1;32;40m[----------HACKING----------] 

 \033[97m[7] Zone-H Grabber                                                
 \033[1;35;40m[8] Bing Dorker HOT!!          
 \033[1;32;40m[9] Mass Reverse Domains => IPs          
 \033[35m[10] Mass IPS Ranger                                                
 \033[97m[11] Mass Laravel, Wordpress Filter NEW!!                                
 \033[91m[12] MASS BYPASS & UPLOAD SHELL  HOT!!                       
 \033[92m[13] Auto Exploit & Upload Shell NEW!!                                                     
 \033[94m[14] Find Path KcFinder NEW!!
 \033[93m[15] Website Grabber TLD NEW!! HOT!! & POPULAR!! 
 \033[94m[16] WPTITAN AUTO EXPLOIT (SHELL PASSWORD IN Results/info.txt) NEW!! HOT!! \033[92m[Recomended IMPROVED]     
 \033[95m[17] CVE-2023-5360 Scan NEW!!
 \033[96m[18] CVE-2023-4666 Scan NEW!!
 \033[91m[19] CVE-2024-2879 Scan NEW!!
 \033[97m[20] Grab And Auto Check Valid phpmyadmin Logins \033[94m[New Feature Added]

\033[1;32;40m[----------OTHER----------] 

 \033[93m[21] Mass DA PA CHECKER  
 \033[94m[22] Auto Traffic (Using Python2)

\033[1;32;40m[----------VIP PRIV8 EXPLOIT (WORDPRESS)----------] 

\033[95m[23] CVE 2024-9593 
\033[96m[24] FI-AD
\033[93m[25] MAMA
\033[97m[26] PLUGINS EXPLOIT
\033[91m[27] W3B-SH311
\033[92m[28] Wp-Back2025
\033[95m[29] WP-OWS
\033[98m[30] WP PLUGIN
\033[97m[31] WP-PRIV8 BackDoor
\033[93m[32] WP-PRIV8
\033[94m[33] GOOGLE EXPLOIT
''')

print(logo)
print(banner)

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
    os.system('python3 Scripts/grabtld/tld.py')
if choice == '16':
    os.system('python3 Scripts/titan/wptitan.py')
if choice == '17':
    target = input(f'{gr}Give Me Your Target ex http://fbi.gov{wh}/{red} > {gr}${res} ')
    os.system('python3 Scripts/CVE-2023-5360/CVE-2023-5360.py '+ target)
if choice == '18':
    target = input(f'{gr}Give Me Your Target ex https://fbi.gov{wh}/{red} > {gr}${res} ')
    os.system('python3 Scripts/CVE-2023-4666/CVE-2023-4666.py '+ target)
if choice == '19':
    target = input(f'{gr}Give Me Your Target ex https://fbi.gov{wh}/{red} > {gr}${res} ')
    os.system('python3 Scripts/CVE-2024-2879/CVE-2024-2879.py '+ target)
if choice == '20':
    target = input(f'{gr}Give Me Your Target ex list.txt{wh}/{red} > {gr}${res} ')
    os.system('python3 Scripts/databaselog/db.py '+ target)
if choice == '21':
    os.system('python3 Scripts/da.py')
if choice == '22':
    os.system('python2 Scripts/AutoVisitor/main.py')
if choice == '23':
    os.system('python3 Scripts/PRIV8/CVE-2024-9593.py')
if choice == '24':
    target = input(f'{gr}Give Me Your Target ex list.txt{wh}/{red} > {gr}${res} ')
    os.system('python3 Scripts/PRIV8/FI-AD.py '+ target)
if choice == '25':
    target = input(f'{gr}Give Me Your Target ex list.txt{wh}/{red} > {gr}${res} ')
    os.system('python3 Scripts/PRIV8/mama.py '+ target)
if choice == '26':
    target = input(f'{gr}Give Me Your Target ex list.txt{wh}/{red} > {gr}${res} ')
    os.system('python3 Scripts/PRIV8/plugins-exploit.py '+ target)
if choice == '27':
    target = input(f'{gr}Give Me Your Target ex list.txt{wh}/{red} > {gr}${res} ')
    os.system('python3 Scripts/PRIV8/W3B-SH311.py '+ target)
if choice == '28':
    target = input(f'{gr}Give Me Your Target ex list.txt{wh}/{red} > {gr}${res} ')
    os.system('python3 Scripts/PRIV8/Wp-Back2024.py '+ target)
if choice == '29':
    target = input(f'{gr}Give Me Your Target ex list.txt{wh}/{red} > {gr}${res} ')
    os.system('python3 Scripts/PRIV8/wp-ows.py '+ target)
if choice == '30':
    target = input(f'{gr}Give Me Your Target ex list.txt{wh}/{red} > {gr}${res} ')
    os.system('python3 Scripts/PRIV8/WP-plugin.py '+ target)
if choice == '31':
    target = input(f'{gr}Give Me Your Target ex list.txt{wh}/{red} > {gr}${res} ')
    os.system('python3 Scripts/PRIV8/WP-Priv8-Backdoor.py '+ target)
if choice == '32':
    target = input(f'{gr}Give Me Your Target ex list.txt{wh}/{red} > {gr}${res} ')
    os.system('python3 Scripts/PRIV8/WP-PRIV8.py '+ target)
if choice == '33':
    target = input(f'{gr}Give Me Your Target ex list.txt{wh}/{red} > {gr}${res} ')
    os.system('python3 Scripts/PRIV8/google-exploit.py '+ target)