import xml.etree.ElementTree as ET

input = '''<stuff>
                <users>
                    <user x="2">
                        <id>101</id>
                        <name>Chuck</name>
                    </user>
                    <user x="7">
                        <id>109</id>
                        <name>Brent</name>
                    </user>
                </users>
           </stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print ('Number of user tags:', len(lst))
for item in lst:
    print ('id:', item.find('id').text)
    print ('name:', item.find('name').text)
    print ('Attribute:', item.get('x'))
