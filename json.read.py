import json
# f=open("sample3.json",'r')
# content=json.load(f)
# print(content)

data=[

    {"name":"adhil","age":20},
    {"name": "adhi", "age": 22}

    ]

f=open("data.json","w")
json.dump(data,f)