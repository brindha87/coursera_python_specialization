# Write a Python program which prompts for a URL, read the XML data from that URL using urllib and
# then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter a url: ')
url_handle = urllib.request.urlopen(url)
data = url_handle.read()
xmldata = data.decode()

tree = ET.fromstring(xmldata) # fromstring returns a tree. 
lst = tree.findall('.//count') #finds comments/comment/count

sum = 0
for item in lst:
    val = int(item.text)
    sum += val

print ('Sum:', sum)

# Use the below url to test this program
# http://py4e-data.dr-chuck.net/comments_42.xml
# Expected output: 2553
# http://py4e-data.dr-chuck.net/comments_141616.xml
# Expected output: 2172
