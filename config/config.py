import typing as tp
import logging
import yaml
from importlib.resources import files


def read_config() -> tp.Dict[str, str]:

    try:
        content = files("Telegram_bot_robonomics_coffeemaker.config").joinpath("config.yaml").read_text()
        config = yaml.load(content, Loader=yaml.FullLoader)
        logging.debug(f"Configuration dict: {content}")
        return config
    except OSError as e:
        logging.error("Error in configuration file!")
        logging.error(e)
        exit()


read_config()