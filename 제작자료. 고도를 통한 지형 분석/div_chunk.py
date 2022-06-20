import json

ll = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"Gijang","Gijang",0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"Gijang","Gijang",0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"Gijang","Gijang",0,0,0,0,"Gijang",0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"Gijang","Gijang","Gijang","Gijang",0,"Gijang","Gijang","Gijang","Gijang"],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"Gijang","Gijang",0,"Gijang","Gijang","Gijang",0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"Gemjeong","Gemjeong",0,0,"Gijang","Gijang",0,0,"Gijang","Gijang","Gijang",0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"Gemjeong","Gemjeong",0,"Gijang","Gijang","Gijang",0,0,"Gijang","Gijang",0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,"Bukgu",0,0,0,0,"Gemjeong",0,0,0,0,0,"Gijang","Gijang","Gijang","Gijang",0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,"Bukgu","Bukgu",0,0,0,"Gemjeong",0,0,0,0,"Gijang",0,"Gijang","Gijang","Gijang",0,0],
    [0,0,0,0,0,0,0,0,0,"Gangseo","Gangseo","Gangseo","Gangseo","Bukgu",0,0,0,"Gemjeong","Gemjeong","Gemjeong","Heaundea","Heaundea","Heaundea",0,0,"Gijang","Gijang",0,0,0],
    [0,0,0,0,0,"Gangseo","Gangseo",0,"Gangseo","Gangseo","Gangseo","Gangseo","Bukgu","Bukgu","Bukgu","Bukgu","Dongnae","Dongnae","Dongnae","Dongnae","Heaundea",0,0,0,0,"Gijang","Gijang",0,0,0],
    [0,0,0,0,0,"Gangseo","Gangseo","Gangseo","Gangseo","Gangseo","Gangseo","Sasang","Sasang","Bukgu",0,0,"Yeonje","Yeonje","Yeonje","Dongnae","Heaundea",0,0,0,0,"Gijang","Gijang",0,0,0],
    [0,0,0,0,0,0,"Gangseo","Gangseo","Gangseo","Gangseo","Gangseo","Sasang","Sasang",0,"Jingu","Jingu","Jingu","Yeonje","Yeonje","Suyeong","Suyeong",0,"Heaundea","Heaundea",0,0,0,0,0,0],
    [0,0,0,0,"Gangseo",0,0,0,0,"Gangseo","Gangseo","Sasang","Sasang","Sasang","Jingu","Jingu","Jingu","Jingu",0,"Suyeong","Suyeong","Heaundea","Heaundea","Heaundea",0,0,0,0,0,0],
    [0,0,0,0,"Gangseo","Gangseo","Gangseo",0,0,"Gangseo","Gangseo","Sasang","Sasang","Sasang","Jingu","Dong-gu","Dong-gu","Nam-gu","Nam-gu","Nam-gu",0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,"Gangseo",0,0,0,0,"Gangseo","Gangseo","Sasang",0,0,0,"Dong-gu","Dong-gu","Nam-gu","Nam-gu","Nam-gu",0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,"Gangseo","Gangseo","Gangseo","Gangseo",0,"Saha","Saha","Saha","Seo-gu","Jung-gu","Jung-gu",0,"Nam-gu","Nam-gu","Nam-gu","Nam-gu",0,0,0,0,0,0,0,0,0],
    [0,0,"Gangseo","Gangseo","Gangseo","Gangseo",0,"Gangseo","Gangseo",0,"Saha","Saha","Saha","Seo-gu","Seo-gu","Youngdo","Youngdo","Youngdo",0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,"Saha","Saha","Saha","Seo-gu","Seo-gu","Youngdo",0,"Youngdo",0,0,0,0,0,0,0,0,0,0,0,0],
    [0,"Gangseo","Gangseo",0,0,0,0,0,0,0,"Saha","Saha","Saha","Seo-gu",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,"Saha","Saha","Saha",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
rll = []
res = []


lat = [3522, 3521,3520, 3519, 3518, 3517, 3516, 3515, 3514, 3513, 3512, 3511, 3510, 3509, 3508, 3507, 3506, 3505, 3504, 3503, 3502, 3501, 3500, 3459]
lng = [12847, 12848, 12849, 12850, 12851, 12852, 12853, 12854, 12855, 12856, 12857, 12858, 12859, 12900, 12901, 12902, 12903, 12904, 12905, 12906, 12907, 12908, 12909, 12910, 12911, 12912, 12913, 12914, 12915, 12916, 12917]
for i in range(0, 24):
    for j in range(0, 30):
        data = ll[i][j]
        if data != 0:
            temp = {}
            temp["id"] = data
            temp["lat_sp"] = int(str(lat[i])[0:2]) + int(str(lat[i])[2:4])/60
            temp["lat_ep"] = int(str(lat[i]+1)[0:2]) + int(str(lat[i]+1)[2:4])/60
            temp["lng_sp"] = int(str(lng[j])[0:3]) + int(str(lng[j])[3:5])/60
            temp["lng_ep"] = int(str(lng[j]+1)[0:3]) + int(str(lng[j]+1)[3:5])/60
            res.append(temp)
            
file_path = "chunk.json"    

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(res, file, indent="\t")
print(res)