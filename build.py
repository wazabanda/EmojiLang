import json
import os

codeName = "main.emo"
splitName = codeName.split(".")
code = open(os.path.join(".", codeName), "r", encoding="UTF8")
splitCode = code.read().split("!")


syntax = json.load(
    open(
        os.path.join('.', 'map.json'),
        'r', encoding="UTF8"))

syntaxList = list(syntax.keys())
with open(os.path.join(".", f"{splitName[0]}.py"), "w") as f:
    for word in splitCode:
        if word == "":
            continue
        else:
            if word in syntaxList:
                f.write(syntax[word])
            else:
                f.write(word)
