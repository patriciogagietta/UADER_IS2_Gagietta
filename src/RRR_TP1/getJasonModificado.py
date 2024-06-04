import json, sys
jsonfile = sys.argv[1]

if len(sys.argv) > 2:
    jsonkey = sys.argv[2]   
else:
    jsonkey = "token1"
    
with open(jsonfile, 'r') as myfile:
    data = myfile.read()
obj = json.loads(data)

print (str(obj[jsonkey]))