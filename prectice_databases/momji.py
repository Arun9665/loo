
import json

name = '{"name": "amit"}'
age = '{"age": 22}'
number = '{"number": 7219463969}'

y = json.loads(name)
x = json.loads(age)
z = json.loads(number)

for b in zip(y,x,z):
    print(b)

print(dir(json))