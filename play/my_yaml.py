import yaml


def read_mapping(key):
    with open('profile.yml', 'r') as f:
        return yaml.load(f)[key]


def read_list(key):
    return read_mapping(key)



