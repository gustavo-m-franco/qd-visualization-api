import os
import yaml


def load_config(path):
    env = 'dev'
    if os.environ.get('ENV') is not None:
        env = os.environ.get('ENV')

    config_name = f"config.{env}.yml"
    config_file_path = f"{path}/{config_name}"
    try:
        with open(config_file_path, 'rb') as config_file:
            config_data = yaml.safe_load(config_file)
        return config_data
    except FileNotFoundError as exc:
        raise Exception(f"Config file not found {config_file_path}") from exc
