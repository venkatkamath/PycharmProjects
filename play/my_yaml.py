import yaml
import os


def read_mapping(key):
    profile_file = os.path.join(os.path.dirname(__file__), 'profile.yml')
    with open(profile_file, 'r') as f:
        return yaml.load(f)[key]


def read_list(key):
    return read_mapping(key)



