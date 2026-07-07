#store data in json file
import json
data=[
    {"id":1,"name":"Amna","age":20, "grade":"A"},
    {"id":2,"name":"Zainab","age":25, "grade":"B"},
]
with open("data.json","w") as f:
    json.dump(data,f)
print("data stored in json file")

#read data from json file
with open("data.json","r") as f:
    data = json.load(f)
    print(data)

#update data in json file
with open("data.json","r") as f:
    data = json.load(f)
for s in data:
    if s["id"] == 1:
        s["grade"] = "A+"
        break

with open("data.json","w") as f:
    json.dump(data,f)

#add new data to json file
import json

with open("data.json", "r") as f:
    data = json.load(f)
new_stu = {"id": 3, "name": "Bilal", "age": 21, "grade": "B+"}
data.append(new_stu)

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print("New student added.")