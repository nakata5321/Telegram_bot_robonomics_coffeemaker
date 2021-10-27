from .lib.telegram_bot import bot_sent_message
from .config.config import read_config
import logging


def main() -> None:
    # set up logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s",
    )
    logging.info("reading config file")
    config = read_config()

    logging.info("send message to coffee delivers")
    bot_sent_message(config["bot_token"], config["bot_chat_id"],
                     "./Telegram_bot_robonomics_coffeemaker/misc/message.ogg")


if __name__ == '__main__':
    main()
