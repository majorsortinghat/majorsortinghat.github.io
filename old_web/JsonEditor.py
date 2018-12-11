import json

with open("major_Descriptions.json", "r") as read_file:
    data = json.load(read_file)


for major in data:
    data[major]["Quote"] = ""

with open("major_Descriptions_quote.json", "w") as outFile:
    json.dump(data,outFile,indent=4, sort_keys=True)










