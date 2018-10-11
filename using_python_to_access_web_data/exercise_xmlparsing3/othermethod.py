# Write a Python program which will prompt for a URL, read the XML data from that URL using urllib
# and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing
# and the other is the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_141616.xml (Sum ends with 72)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

while True:
    url = input('Enter URL: ')
    if len(url) < 1: break
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')

    sum = 0
    for item in counts:
        val = int(item.text)
        sum += val

    print ('Sum:', sum)
