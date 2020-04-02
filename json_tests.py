import requests
import json
import re
from bs4 import BeautifulSoup 
# ploads = {'stream':'abcd','data':38}
# r = requests.get('http://192.168.0.21:8069/iot/stream',params=ploads)
# print(r.text)
# print(r.url)

payload = {     'name' : 'Attendance_Terminal_1' ,
                'location' :  'Lobby_first_floor'}

r = requests.get('http://192.168.0.31:8069/things/gates/create?name=Attendance_Terminal_1&location=_Lobby_first_floor')
htmlText = r.text
print(htmlText)
htmlText = htmlText.replace("'", '"') # TextWithDoubleQuotes
htmlText = htmlText.replace("<script> data1 = ", '')
htmlText = htmlText.replace("</script>", '')
print ('Prepared ############### \n \n',htmlText)
# print(r.url) 


print('json: ########### \n \n\n\n #######\n\n', json.loads(htmlText))


# soup = BeautifulSoup(html_text, features="html.parser")

# script = soup.find('script', text=re.compile("data1"))

# scriptWithDoubleQuotes = script.string

#print(scriptWithDoubleQuotes)

# scriptWithDoubleQuotes = "{'data1': [{'id': 9, 'name': 'Agrolait'}, {'id': 19, 'name': 'Edward Foster'}]}"
# scriptWithDoubleQuotes = scriptWithDoubleQuotes.replace("'", '"')
# print(scriptWithDoubleQuotes)

#scriptWithDoubleQuotes = scriptWithDoubleQuotes.replace("[", '{')
#scriptWithDoubleQuotes = scriptWithDoubleQuotes.replace("]", '}')

#{"data1": [{'id': 9, 'name': 'Agrolait'}, {'id': 19, 'name': 'Edward Foster'}, {'id': 34, 'name': 'Laith Jubair'}, {'id': 24, 'name': 'Michel Fletcher'}, {'id': 23, 'name': 'Thomas Passot'}, {'id': 8, 'name': 'ASUSTeK'}, {'id': 20, 'name': 'Arthur Gomez'}, {'id': 18, 'name': 'James Miller'}, {'id': 16, 'name': 'Joseph Walters'}, {'id': 21, 'name': 'Julia Rivero'}, {'id': 22, 'name': 'Peter Mitchell'}, {'id': 15, 'name': 'Tang Tsui'}, {'id': 13, 'name': 'Camptocamp'}, {'id': 31, 'name': 'Ayaan Agarwal'}, {'id': 37, 'name': 'Benjamin Flores'}, {'id': 30, 'name': 'Phillipp Miller'}, {'id': 10, 'name': 'China Export'}, {'id': 25, 'name': 'Chao Wang'}, {'id': 26, 'name': 'David Simpson'}, {'id': 36, 'name': 'Jacob Taylor'}, {'id': 27, 'name': 'John M. Brown'}, {'id': 11, 'name': 'Delta PC'}, {'id': 28, 'name': 'Charlie Bernard'}, {'id': 29, 'name': 'Jessica Dupont'}, {'id': 41, 'name': 'Kevin Clarke'}, {'id': 40, 'name': 'Morgan Rose'}, {'id': 17, 'name': 'Richard Ellis'}, {'id': 35, 'name': 'Robert Anderson'}, {'id': 39, 'name': 'Robin Smith'}, {'id': 45, 'name': 'Forgeflow SL'}, {'id': 46, 'name': 'Steven Hamilton'}, {'id': 1, 'name': 'luintel '}, {'id': 42, 'name': 'Mark Davis'}, {'id': 43, 'name': 'Roger Scott'}, {'id': 12, 'name': 'The Jackson Group'}, {'id': 32, 'name': 'Daniel Jackson'}, {'id': 33, 'name': 'William Thomas'}, {'id': 14, 'name': 'Think Big Systems'}, {'id': 38, 'name': 'Lucas Jones'}, {'id': 3, 'name': 'Administrator'}, {'id': 7, 'name': 'Demo Portal User'}, {'id': 6, 'name': 'Demo User'}] };

# jsonText = re.search(r'^\s*data1\s*=\s*({.*?})\s*;\s*$',
#             scriptWithDoubleQuotes,
#             flags=re.DOTALL | re.MULTILINE).group(1)


# jsonText = scriptWithDoubleQuotes

# data = json.loads(jsonText)

# print(data)