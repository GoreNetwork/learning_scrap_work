import json

crap_data = '{"name":"John", "age":30, "car":null}'

json_data = json.loads(crap_data)



for x in range(1,20):
    json_data['age']=json_data['age']+1
    print (json.dumps(json_data))