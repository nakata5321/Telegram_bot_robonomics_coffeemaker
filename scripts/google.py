from gtts import gTTS
from pydub import AudioSegment

"""
this program convert to speech with Google TTS and save it as .mp3 and .ogg files 
"""
#
tts = gTTS('Принеси мне кофе, кожаный мешок', lang='ru')
tts.save('output.mp3')

song = AudioSegment.from_mp3("../misc/output.mp3").export('../misc/message.ogg', format='ogg')
