import requests


def telegram_bot_sendtext(bot_message):
    bot_token = '2062171338:AAExSL35b7YW1ZmskdE3K_olMk3BHUQKYDc'
    bot_chat_id = '441944588'
    send_text = 'https://api.telegram.org/bot' + bot_token \
                + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


message = """
    Ваша оплата - \
    https://statemine.subscan.io/extrinsic/0xe7c9d075f1dd06616442a2606929547a69bb644b62211f215670bf7971e62d4d
    """
test = telegram_bot_sendtext(message)
print(test)
