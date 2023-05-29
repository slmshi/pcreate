import json
import os

path = "1.8.9\\assets\\minecraft\\textures"
nextlist = {
    
}

def createjsonfiles(nextlist):
    keys = list(nextlist.keys())
    for i in keys:
        with open(f"{i}.json", "w") as f:
            json.dump(nextlist[i], f)

def searchpath(nextlist):
    for i in os.listdir(path):
        nextpath = f"{path}\\{i}"
        nextlist[i] = os.listdir(nextpath)
    return nextlist

nextlist = searchpath(nextlist)
createjsonfiles(nextlist, path)
