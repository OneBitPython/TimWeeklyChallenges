import json

with open("cases.json") as f:
    g = json.loads(f.read())

for data in g:
    inputs = data["Input"]
    output = data["Output"]

    if "discord" in inputs:
        h = inputs.index("discord")
        print(inputs[h - 9 : h + 78])