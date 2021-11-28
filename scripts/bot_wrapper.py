import telegram

bot_token = ''
bot_chat_id = ''

bot = telegram.Bot(token=bot_token)

print(bot.get_me())
updates = bot.get_updates()
print(updates[0])

with open("result.ogg", 'rb') as audio:
    bot.send_voice(bot_chat_id, audio, filename="test", parse_mode="HTML", duration=4)
