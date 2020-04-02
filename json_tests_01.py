import requests
import json

payload =  {"params" : {  "name" : "Attendance Terminal 4" ,
                "location" :  "Lobby first floor"} }

url = 'http://192.168.0.31:8069/things/gates/create'

headers = {'content-type': 'application/json'}

r = requests.post(url,
    data=json.dumps(payload),
    headers=headers)

gateData = json.loads(r.text)

#print ('raw json dictionary received', gateData)


if 'result' in gateData.keys():
    if gateData['result']:
        print('New Gate Created\n', gateData)
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