import json

with open('c.html', 'r') as test_convert:
    s = test_convert.read()
    s2 = json.dumps(s)
    print(s2)
    