import json


json_file_path = ""  # insert path

with open(json_file_path, encoding='utf-8-sig') as json_data:
    data = json.load(json_data, strict=False)
    types = list(data['players'][0].keys())
    print(types)
    print(len(list(data['players'])))
    print(data['players'][0]['nickname'])
    print(type(json.dumps(data, indent=3, sort_keys=True)))
    print()
    print(data["bossId"])
    print("\n\n\n")
    players = data['players']
    for player in players:
        for v in types:
            print(v, end = " ")
            print(player[v])
