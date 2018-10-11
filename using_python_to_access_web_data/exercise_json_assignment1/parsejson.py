# Write a Python program which will prompt for a URL, read the JSON data from that URL using urllib
# and then parse and extract the comment counts from the JSON data,
# and compute the sum of the numbers in the file

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_141617.json (Sum ends with 38)

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter URL: ')
    if len(url) < 1: break
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)

    sum = 0
    for item in js["comments"]:
        sum += item["count"]

    print ('Sum:', sum)
