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
                
                with open(f"data/generated/utterance/{intent_name}.txt", mode = "w+") as intent_file:
                    for i, name in enumerate(utterances):
                        # print("Index: ", i, "\tLength:", len(utterances) - 1)
                        if len(utterances) -1 == i:
                            newline = ""  # To remove new line at the end of file.
                        intent_file.write(name + newline)  # Adding data to text file with new line.

            elif intent_type == "entity":
                entity_values = str(item["values"])
                with open(f"data/generated/entity/{intent_name}.txt", mode = "w+") as entity_file:
                    entity_file.write(entity_values) 
                    
        return "Text files created successfully."


file_to_convert = "data/dataset.yaml"
print(yamltotext(file_to_convert))