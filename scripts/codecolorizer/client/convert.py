import json

with open('test-convert.html', 'r') as test_convert:
    s = test_convert.read()
    s2 = json.dumps(s)
    print(s2)
    