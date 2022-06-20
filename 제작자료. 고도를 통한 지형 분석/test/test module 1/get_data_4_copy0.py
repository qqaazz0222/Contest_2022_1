import requests
import json
import numpy

lat = 0
lng = 0
i = 0
j = 0
file_path = ""
selected_data = []
ll_gu = ['Jung-gu', 'Youngdo']

with open('chunk.json', 'r') as f:
    chunk_data = json.load(f)

for lg in ll_gu:
    for cd in range(0, len(chunk_data)):
        gu = chunk_data[cd]["id"]
        if gu == lg:
            print(gu, lg)
            file_path = "res/" + gu + ".json"
            lat_sp = chunk_data[cd]["lat_sp"]
            lat_ep = chunk_data[cd]["lat_ep"]
            lng_sp = chunk_data[cd]["lng_sp"]
            lng_ep = chunk_data[cd]["lng_ep"]
            for lat in numpy.arange(lat_sp, lat_ep, (1/300)):
                for lng in numpy.arange(lng_sp, lng_ep, (1/300)):
                    url = "https://maps.googleapis.com/maps/api/elevation/json" #openApi URL
                    location = "?locations=" + str(lat) + ", " + str(lng)
                    sensor = "&sensor=false"
                    serviceKey = "&key=AIzaSyCoN4YlT7Lb58Di68B0Yw_f8yB3JM21D0c" #서비스 키
                    requestURL = url + location + sensor + serviceKey

                    res = requests.get(requestURL) 

                    items = res.json().get('results') #가져온 데이터 중 아이템들만 추출
                    if str(items[0]['elevation']) != '0':
                        temp = {}
                        temp['location'] = gu
                        temp['lat'] = lat
                        temp['lng'] = lng
                        temp['elevation'] = str(items[0]['elevation'])
                        selected_data.append(temp)
                        # print(temp)
    
    with open(file_path, 'w', encoding='utf-8') as make_file:
        json.dump(selected_data, make_file, indent="\t")
    print(selected_data)
    selected_data = []