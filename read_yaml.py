import yaml  # pip install pyyaml (PyPi - Python Package Index)


def yamltotext(filename):
    with open(filename, "r") as yaml_file:
        file_data = yaml.load_all(yaml_file, Loader=yaml.FullLoader)


file_to_convert = "data/dataset.yaml"
yamltotext(file_to_convert)