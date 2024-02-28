import pygame
from openai import OpenAI
import sensitiveData
import os

import warnings

API_KEY = sensitiveData.apiKey
client = OpenAI(api_key=API_KEY)

def play_audio(audio_file):
    pygame.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def ttsPlay(text):
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    response = client.audio.speech.create(
        model="tts-1",
        voice="shimmer",
        input=text,
    )
    response.stream_to_file("output.mp3")

    play_audio("output.mp3")
    os.remove("output.mp3")

if __name__ == "__main__":
    ttsPlay("Hello World!")
