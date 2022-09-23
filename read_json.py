import json
import objectpath  # Needs to be installed -> pip install objectpath

with open("data/test.json", mode="r", encoding="utf-8") as json_file:
    data = json.load(json_file)  # Loads the file object returned from open as python data file.
    tree = objectpath.Tree(data)  # data["keyname"]
    result = tuple(tree.execute("$..value"))

print(json.dumps(result, indent=4, sort_keys=True))
