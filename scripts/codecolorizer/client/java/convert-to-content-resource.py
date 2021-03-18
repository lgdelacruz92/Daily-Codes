import json
import sys

with open(sys.argv[1],'r') as test_convert:
    s = test_convert.read()
    s2 = json.dumps(s)
    print(s2)
    