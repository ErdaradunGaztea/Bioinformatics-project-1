import yaml


def parse_config(filename):
    with open(filename) as f:
        config = yaml.safe_load(f)
    return config
