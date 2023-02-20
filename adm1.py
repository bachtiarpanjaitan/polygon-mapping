import json

file_adm = open('mapping/adm1-db.json')
file_pol = open('mapping/adm1-polygon.json')
output = open('mapping/output/adm1.json','w')

data = json.load(file_adm)
data_pol = json.load(file_pol)

temp_data = []

for i,item in enumerate(data['features']):
    prop = item['properties']
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