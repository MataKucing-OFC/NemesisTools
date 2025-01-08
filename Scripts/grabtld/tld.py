# -*- coding: utf-8 -*-
#!usr/bin/python
import os, re, sys, socket, json
import requests as req
from multiprocessing.dummy import Pool
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from colorama import *

init(autoreset=True)

fg = '\033[0;32m'
fr = '\033[0;31m'
fw = '\033[1;37m'
fb = '\033[0;34m'
fy = '\033[1;33m'
fre = '\033[0m'

Headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
def zone(dom):
  page = 0
  while True:
    page += 1
    f = req.get('http://pluginu.com/domain-zone/'+dom+'/'+str(page))
    g = re.findall('<button class="btn btn-default pull-left" type="button">\n  (.*?)</button></a>', f.text)
    if g == '':
      print('EndPage')
      sys.exit()
    else:
      for domain in g:
        print('[{}] >> [{}]'.format(str(page), g))
        save = open('Results/'+dom+'.txt', 'a')
        save.write('http://'+domain+'\n')
        save.close()
tld = input('enter Tld. Domain : ')
zone(tld)
