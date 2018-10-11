# Write a Python program that will use urllib to read the HTML from the data files below, and parse the data,
# extracting numbers and compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_141614.html (Sum ends with 91)

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
tags = soup('span')

sum = 0
for tag in tags:
    val = int(tag.contents[0])
    sum += val

print ('Sum:', sum)
