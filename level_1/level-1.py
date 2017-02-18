#!/usr/bin/python3
"""
This module votes for id 77 at given url using requests.
"""
import requests


url = 'http://54.221.6.249/level1.php'
payload = {'id': '77', 'holdthedoor': 'Submit+Query', 'key': ''}
cookies = {'HoldTheDoor': '', 'holdthedoor': ''}
cookies['holdthedoor'] = requests.get(url).cookies['HoldTheDoor']
for i in range(4096):
    r = requests.post(url, data=payload, cookies=cookies)
    print(r.text)
