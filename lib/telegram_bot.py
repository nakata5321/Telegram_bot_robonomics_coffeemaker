import requests
import logging


def bot_sent_message(token: str, chat_id: str, path: str) -> None:
    """
    send voice message and text message to given chat id.
    :param token: unique Bot token
    :param chat_id:unique int id of chat
    :param path: path to the voice message
    """
    logging.info(f"sent voice message to {chat_id} chat")
    # send voice message
    with open(path, 'rb') as audio:
        payload = {
            'chat_id': chat_id,
            'parse_mode': 'HTML'
        }
        voice = {
            'voice': audio.read(),
        }
        resp = requests.post(
            "https://api.telegram.org/bot{token}/sendVoice".format(token=token),
            data=payload,
            files=voice)
        logging.info(resp.json())

    # sent Text message
    logging.info("sent text message")
    bot_message = """
    адрес доставки - улица Фрунза 8аа, этаж - 3, квартира - 220.\
    Временный пароль от домофона - 11422. Пароль действителен в течение 24 часов.
    """
    send_text = 'https://api.telegram.org/bot' + token \
                + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    logging.info(response.json())

