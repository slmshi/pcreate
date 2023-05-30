import json
import os

path = "1.8.9\\assets\\minecraft\\textures"

pathes = list(os.walk(path))
paths = []

folders = []
for i in pathes:
    folders.append([i[0]])
    with open(f"{i[0]}\\{os.path.basename(i[0])}.json", "w") as f:
        json.dump(i[2], f)

with open("dirs.json", "w") as f:
    json.dump(folders, f)
