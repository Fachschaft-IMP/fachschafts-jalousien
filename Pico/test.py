import json
test = '{"id": "jalou-slider1","volume": "36"}'
test = '{"id": "masster-slider","volume": "36"}'

jsonString = json.loads(test)

id = 0
if jsonString:
    print(jsonString)
    data = json.loads(test)
    idString = data['id']
    value = data['volume']
    try:
        # für einzelne Motoren hier
        id = int(idString[-1])
    except:
        # Master slider shit hier
        print("Master-slider")
        pass

print(id)
