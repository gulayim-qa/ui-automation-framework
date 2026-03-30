import yaml


class ConfigReader:
    with open("selenium_tests/default_config.yml", "r") as file:
        _config = yaml.safe_load(file)

    try:
        with open("selenium_tests/config.yml", "r") as file:
            _config = yaml.safe_load(file)
    except FileNotFoundError:
        pass

    @classmethod
    def get_config_value(cls, key):
        keys = key.split(".")
        value = cls._config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return None
        return value
