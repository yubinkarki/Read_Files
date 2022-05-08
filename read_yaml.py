import yaml  # pip install pyyaml (PyPi - Python Package Index)


def yamltotext(filename):
    with open(filename, "r") as yaml_file:
        file_data = yaml.load_all(yaml_file, Loader=yaml.FullLoader)
        
        for item in file_data:
            intent_type = item["type"]
            intent_name = item["name"]
            newline = "\n"

            if intent_type == "intent":
                utterances = item["utterances"]
                
                with open(f"data/Text_Files/{intent_name}.txt", mode = "w+") as intent_file:
                    for i, name in enumerate(utterances):
                        # print("Index: ", i, "\tLength:", len(utterances) - 1)
                        if len(utterances) -1 == i:
                            newline = ""  # To remove new line at the end of file.
                        intent_file.write(name + newline)  # Adding data to text file with new line.
        
        return "Text files created successfully."


file_to_convert = "data/test.yaml"
print(yamltotext(file_to_convert))