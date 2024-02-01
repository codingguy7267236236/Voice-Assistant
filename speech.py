import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

#speak
def speak(text):
    #creates audio file
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    #saves file
    tts.save(filename)

    playsound.playsound(filename)

    
