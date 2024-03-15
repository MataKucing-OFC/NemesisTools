

import asyncio
import aiohttp
from aiohttp import ClientSession
import time
import socket
import os
print(f'''
 _  ______ _____ ___           _           
| |/ / ___|  ___|_ _|_ __   __| | ___ _ __ 
| ' / |   | |_   | || '_ \ / _` |/ _ \ '__|
| . \ |___|  _|  | || | | | (_| |  __/ |   NEMESIS FREE TOOLS
|_|\_\____|_|   |___|_| |_|\__,_|\___|_|   GITHUB : MataKucing-OFC
''')
target = input("Url: \33[1;0m")
print("")

target = target.replace('https://', '')
target = target.replace('http://', '')
tar_list = target.split('/')
for tar in tar_list:
    if tar == '':
        tar_list.remove(tar)
target = '/'.join(tar_list)
target = 'http://' + target

start = time.time()

yay = []

conn = aiohttp.TCPConnector(
        family=socket.AF_INET,
        verify_ssl=False,
    ) 

async def fetch(url, session):
    async with session.get(url) as response: 
        status = response.status 
        if status == 200:
            print("\33[97;1mFound It >->  \33[1;0m{}\33[97;1m  Status {}".format(response.url, status))
            yay.append(response.url)
        elif status == 404:
            print("\33[91;1mxXx \33[94;1m{}\33[91;1m Status {}".format(response.url, status))
        elif status == 403:
            print("\33[91;1mxXx \33[94;1m{}\33[91;1m Status \33[95;1m{}".format(response.url, status))
        else:
            print("\33[95;1m??? {} Status {}".format(response.url, status))
        return await response.read()

async def run():
    url = target + "{}"
    tasks = []
    admin_list = open('wordlist.txt', 'r')
    paths = []
    for path in admin_list:
        path = path.replace('\n','')
        paths.append(path)

    async with ClientSession(connector=conn) as session: 
        for i in paths:
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses
        
     
loop = asyncio.get_event_loop()

future = asyncio.ensure_future(run())
loop.run_until_complete(future)


end = time.time()
script_time = end - start
print("\33[93;1mScan took {} seconds to complete\n".format(script_time))
print("\33[91;1m### \33[93;1mResults \33[91;1m###\33[1;0m")
if len(yay) == 0:
    print("\33[94;1m!!! No Results !!!")
    os.system('python3 find.py')   
else:
    for y in yay:
        print(y)    
print("\33[91;1m##################################\033[0m")
os.system('python3 find.py')   
