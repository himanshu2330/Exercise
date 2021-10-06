input.json
{"a":{"b":{"c":"d"}}}

========
import json
with open('./input.json') as access_json:
    read_content = json.load(access_json)
key = []

def return_keys():
    key_data =  read_content['a']
    for data in key_data:
        key_new = data['b']
            for data1 in key_new:
                key_value = key_new['c']
                keys.append(key_value)


return_keys

