import typing as tp
import logging
import yaml
import os
from scripts.telegram_bot import bot_sent_message


def read_config(path: str) -> tp.Dict[str, str]:

    config_path = path + 'config/config.yaml'
    logging.debug(config_path)

    try:
        with open(config_path) as f:
            content = f.read()
            config = yaml.load(content, Loader=yaml.FullLoader)
            logging.debug(f"Configuration dict: {content}")
            return config
    except Exception as e:
        while True:
            logging.error("Error in configuration file!")
            logging.error(e)
            exit()


def main() -> None:
    # set up logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s",
    )
    logging.info("reading config file")
    dirname = os.path.dirname(__file__)
    logging.info(dirname)
    config = read_config(dirname)

    logging.info("send message to coffee delivers")
    bot_sent_message(config["bot_token"], config["bot_chat_id"], "misc/message.ogg")


if __name__ == '__main__':
    main()
