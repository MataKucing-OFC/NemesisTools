# -*- coding: utf-8 -*-

import sys , requests, re, random, string
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
 
init(autoreset=True)
fr  =   Fore.RED
fg  =   Fore.GREEN
fw = Fore.WHITE
requests.urllib3.disable_warnings()
p = ''' 
 NEMESIS TOOLS
'''

print(fg + p + Fore.WHITE)
         
try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

Pathlist = ['themes.php','admin.php']

class Nemesis_Tools:
	def __init__(self):

		self.headers = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}

	
	def URLdomain(self, site):
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
		
	def NemesisTools(self, site):
		try:
			
			url = "http://" + self.URLdomain(site)
			for Path in Pathlist:
				check = requests.get(url +'/'+ Path, headers=self.headers, verify=False, timeout=25).content
				if("<title>403WebShell</title>" in check or 'User :' in check or "LinuXploit" in check or "????JFIF??x?x????" in check ):
					print(' NemeSis TOOLS :{} --> {}[Succefully]').format(url, fg)
					open('Results/VIP-VULN.txt','a').write(url +'/'+ Path + "\n")
					break
				else:
					print(' NemeSis TOOLS :{} -->! {}[Failid]').format(url, fr)		
		except:
			pass

	
Control = Nemesis_Tools()	
def NemeSis(site):
	try:
		Control.NemesisTools(site)
	except:
		pass
mp = Pool(150)
mp.map(NemeSis, target)
mp.close()
mp.join()