import telegram

bot_token = '2062171338:AAExSL35b7YW1ZmskdE3K_olMk3BHUQKYDc'
#bot_chat_id = '360407525' # pasha
#bot_chat_id = '441944588'
bot_chat_id = '176010107' # ylia

bot = telegram.Bot(token=bot_token)

print(bot.get_me())
updates = bot.get_updates()
print(updates[0])

with open("result.ogg", 'rb') as audio:
    bot.send_voice(bot_chat_id, audio, filename="test", parse_mode="HTML", duration=4)
