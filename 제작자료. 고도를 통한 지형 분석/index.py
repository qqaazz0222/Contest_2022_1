import requests
import json
from haversine import haversine


lat = 0
lng = 0
i = 0
j = 0
selected_data = []

# for i in range(348799083, 348909083, 50000):
#     for j in range(1287384361, 1287494361, 50000):

for i in range(348799083, 350114153, 50000):
    for j in range(1287384361, 1293828194, 50000):
        lat = i
        lng = j
        url = "https://maps.googleapis.com/maps/api/elevation/json" #openApi URL
        location = "?locations=" + str(lat / 10000000) + ", " + str(lng / 10000000)
        sensor = "&sensor=false"
        serviceKey = "&key=AIzaSyCoN4YlT7Lb58Di68B0Yw_f8yB3JM21D0c" #서비스 키
        requestURL = url + location + sensor + serviceKey

        res = requests.get(requestURL) 

        items = res.json().get('results') #가져온 데이터 중 아이템들만 추출
        if str(items[0]['elevation']) != '0':
            temp = {}
            temp['lat'] = lat / 10000000
            temp['lng'] = lng / 10000000
            temp['elevation'] = str(items[0]['elevation'])
            selected_data.append(temp)
            print(temp)
    
file_path = "db_1.json"

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(selected_data, file, indent="\t")
print(selected_data)