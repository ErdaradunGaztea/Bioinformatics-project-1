from src.config import parse_config

default_config = {
    "same_award": 2,
    "gap_penalty": 1,
    "difference_penalty": 2,
    "max_seq_length": 10000,
    "max_number_paths": 100
}


def test_parse_config():
    config = parse_config("default_config.yml")
    assert config == default_config
