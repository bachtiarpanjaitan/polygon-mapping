import json

file_adm = open('adm3-db.json')
file_pol = open('adm3-polygon.json')
output = open('output/adm3.json','w')
from shapely.geometry import shape

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
        "name": item['properties']['ADM3_EN'],
        "code": item['properties']['ADM3_PCODE'],
        "adm0": item['properties']['ADM0_EN'],
        "adm0_code": item['properties']['ADM0_PCODE'],
        "adm1": item['properties']['ADM1_EN'],
        "adm1_code": item['properties']['ADM1_PCODE'],
        "adm2": item['properties']['ADM2_EN'],
        "adm2_code": item['properties']['ADM2_PCODE'],
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