import json

ll_gu = ['Gijang', 'Gemjeong', 'Bukgu', 'Gangseo', 'Heaundea', 'Dongnae', 'Sasang', 'Yeonje', 'Jingu', 'Suyeong', 'Dong-gu', 'Nam-gu', 'Saha', 'Seo-gu', 'Jung-gu', 'Youngdo']

rr = []

for i in range(0,len(ll_gu)):
    f = "file_" + str(i)
    d = "data_" + str(i)
    with open('../res/'+ll_gu[i]+".json") as f:
        d = json.load(f)
    temp = {}
    temp[ll_gu[i]] = d
    rr.append(temp)

with open("res.json", "w") as new_file:
    json.dump(rr, new_file, indent="\t")