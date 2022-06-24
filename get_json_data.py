import json
json_data = {
    "features": [
        {
            "geometry":{},
            "properties":{
                "2013_population_estimate":7278717,
                "aland":"294360991275",
                "awater":"858853288",
                "geoid":"04000US04",
                "name":"Arizona"
                },
                 "type":"Feature"
          },
          {
             "geometry":{},
             "properties":{
                "2013_population_estimate":3017804,
                "aland":"134660850501",
                "awater":"3121867339",
                "geoid":"04000US05",
                "name":"Arkansas"
             },
             "type":"Feature"
          },
    ],
    "type":"FeatureCollection"
}

def get_data(x):
    print("__", type(x))
    data = json.dumps(x)
    print("--===", data)
    print("--===", type(data))
    dict_data = json.loads(data)
    print("-++--", dict_data)
    print("-++--", type(dict_data))
    for i in dict_data['features']:
        print("--++--", i['properties']['geoid'])
        print("--++--", i['properties']['name'])
        
    geo_data = list(map(lambda a: a.get('properties').get("geoid"), dict_data['features']))
    print('====-------',geo_data)
    
get_data(json_data)