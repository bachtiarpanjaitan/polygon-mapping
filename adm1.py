import json

file_adm = open('adm1-db.json')
file_pol = open('adm1-polygon.json')
output = open('output/adm1.json','w')

data = json.load(file_adm)
data_pol = json.load(file_pol)

temp_data = []

for i,item in enumerate(data['features']):
    # prop = item['properties']
    prop = {
        "shape_leng": item['properties']['Shape_Leng'],
        "shape_area": item['properties']['Shape_Area'],
        "name": item['properties']['ADM1_EN'],
        "code": item['properties']['ADM1_PCODE'],
        "adm0": item['properties']['ADM0_EN'],
        "adm0_code": item['properties']['ADM0_PCODE'],
        "id":None
    }
    prop['coordinates'] = {
        "type": 'Feature',
        "properties": {},
        "geometry": data_pol['geometries'][i]
    }
    temp_data.append(prop)

json_string = json.dumps(temp_data)
output.write(json_string)
file_adm.close()
file_pol.close()
output.close()