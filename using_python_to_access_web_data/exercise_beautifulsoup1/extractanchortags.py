# For testing this program you can use the link: http://www.dr-chuck.com

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
connection = urllib.request.urlopen(url, context=ctx)
html = connection.read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

for tag in tags:
    print(tag.get('href', None))


# ADDITIONAL INFORMATION FOR REFERENCE:
# Look at the parts of a tag
# print('TAG:', tag)
# print('URL:', tag.get('href', None))
# print('Contents:', tag.contents[0])
# print('Attrs:', tag.attrs)
