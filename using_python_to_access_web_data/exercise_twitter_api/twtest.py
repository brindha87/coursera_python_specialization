import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl

print ('Calling Twitter........')
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
              {'screen_name': 'drchuck', 'count':'2'})
print (url)

# The below 3 lines of code are used to work with https pages without errors
# If you are working with only http, these lines are not needed
# Ignores SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url)
data = connection.read()
print (data)

headers = dict(connection.getheaders())
print (headers)
