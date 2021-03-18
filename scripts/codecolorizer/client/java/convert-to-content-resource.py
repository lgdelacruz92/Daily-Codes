import json
import sys

with open('java_pygments.html','r') as test_convert:
    s = test_convert.read()
    s2 = json.dumps(s)
    print(s2)
    