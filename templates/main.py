import json
import os
txt_file = open("data/info.txt", "rt")
data = txt_file.read()
data = data.replace('|', ' ')
txt_file.close()
txt_file = open("data/info.txt", "wt")
txt_file.write(data)
txt_file.close()

dict1 = {}
with open("data/info.txt") as file:

	for line in file:
            command, description = line.strip().split(None, 1)
            dict1[command] = description.strip()
out_file = open("data.json", "w")
json.dump(dict1, out_file, indent = 4, sort_keys = False)
out_file.close()
query = input("Enter Your Broker Number: ")
text = str(query)
def myfunction(text):
    try:
        with open ("data.json") as file:
	        data = json.load(file)
        return(data[text])
    except:
        error = "This ID doesn't exist"
        return error
    
print(myfunction(text))