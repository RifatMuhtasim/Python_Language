import json

# Convert from JSON to Python
x = '{ "name":"Arnob", "age":30, "city":"London"}'
json_x = json.loads(x)
print(json_x["name"])


# Convert from Python to JSON
y = {"name": "Argo", "age": 54, "city": "Manchester"}
z = json.dumps(y)
print(z)

# use four indents to make it easier to read the result:
print(json.dumps(z, indent=4))
