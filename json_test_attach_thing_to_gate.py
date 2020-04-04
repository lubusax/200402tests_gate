import requests
import json

payload =  {"params" : {  "action" : "new thing" ,
                "thing type" :  "HDC1080",
                "thing identifier" : "C3P5"
                } }

url_basis  = 'http://192.168.0.31:8069/things/gates/incoming/'
routeFrom  ='202004041155497068e4e26e59443fb1ceaec72971a8c0'

url = url_basis + routeFrom

headers = {'content-type': 'application/json'}

r = requests.post(url,
    data=json.dumps(payload),
    headers=headers,
    timeout=1)

gateData = json.loads(r.text)

print ('raw json dictionary received', gateData)


if 'result' in gateData.keys():
    if gateData['result']:
        print('All went well\n', gateData)
    else:
        print ('No new gate created \nAnother Gate must be confirmed \n')
elif 'error' in gateData.keys():
    if gateData['error']['data']['arguments'][0] =='Name must be unique.':
        print('Gate Name is already present in the Database \n'+ \
                'Please choose another Name')
    else:
        print ('Something went wrong. Gate was not created. Try again')
        print('/n/n')
else:
    print('Something unexpected happened. Gate was not created. Try again')