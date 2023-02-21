import json

file_adm = open('adm0-db.json')
file_pol = open('adm0-polygon.json')
output = open('output/adm0.json','w')

data = json.load(file_adm)
data_pol = json.load(file_pol)

temp_data = []

for i,item in enumerate(data['features']):
    prop = {
        "shape_leng": item['properties']['Shape_Leng'],
        "shape_area": item['properties']['Shape_Area'],
        "name": item['properties']['ADM0_EN'],
        "code": item['properties']['ADM0_PCODE'],
        "id":None
    }
    prop['coordinates'] = json.dumps({
        "type": 'Feature',
        "properties": {},
        "geometry": data_pol['geometries'][i]
    })
    temp_data.append(prop)

json_string = json.dumps(temp_data)
output.write(json_string)
file_adm.close()
file_pol.close()
output.close()