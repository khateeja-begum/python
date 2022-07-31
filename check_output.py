from os import path
from pydub import AudioSegment

#files

src = "voice.wav"
dst = "output.mp3"

#convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")