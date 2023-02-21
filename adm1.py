import json
from shapely.geometry import shape

file_adm = open('adm1-db.json')
file_pol = open('adm1-polygon.json')
output = open('output/adm1.json','w')

data = json.load(file_adm)
data_pol = json.load(file_pol)
temp_data = []

for i,item in enumerate(data['features']):
    center = shape(data_pol['geometries'][i]).centroid
    y = center.y
    x = center.x
    prop = {
        "shape_leng": item['properties']['Shape_Leng'],
        "shape_area": item['properties']['Shape_Area'],
        "name": item['properties']['ADM1_EN'],
        "code": item['properties']['ADM1_PCODE'],
        "adm0": item['properties']['ADM0_EN'],
        "adm0_code": item['properties']['ADM0_PCODE'],
        "x": x,
        "y": y,
        "id":None
    }
    prop['coordinates'] = {
        "type": 'FeatureCollection',
        'features': [
            {
                "type": 'Feature',
                "properties": {},
                "geometry": json.dumps(data_pol['geometries'][i])
            }
        ]
    }
    temp_data.append(prop)

json_string = json.dumps(temp_data)
output.write(json_string)
file_adm.close()
file_pol.close()
output.close()