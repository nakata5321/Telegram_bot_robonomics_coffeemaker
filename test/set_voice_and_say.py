import pyttsx3

tts = pyttsx3.init()

voices = tts.getProperty('voices')

# Задать голос по умолчанию

tts.setProperty('voice', 'ru')
tts.setProperty('rate', 150)    # Скорость в % (может быть > 100)

# Попробовать установить предпочтительный голос

for voice in voices:

    ru = voice.id.find('RHVoice\Anna')  # Найти Анну от RHVoice

    if ru > -1: # Eсли нашли, выбираем этот голос

        tts.setProperty('voice', voice.id)

tts.say('Командный голос вырабатываю, товарищ генерал-полковник!')

tts.runAndWait()