import json

input = '''[
                {"id": "001",
                 "x": "2",
                 "name": "Chuck"
                 },
                 {"id": "009",
                  "x": "5",
                  "name": "Chuck"
                 }
            ]'''

info = json.loads(input)
for item in info:
    print ('id:', item["id"])
    print ('attr:', item["x"])
    print ('name:', item["name"])
