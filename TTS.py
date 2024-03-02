import pygame
from openai import OpenAI
import sensitiveData
import os
import elevenlabs

import warnings

API_KEY = sensitiveData.apiKey
client = OpenAI(api_key=API_KEY)


TTSapiKey=sensitiveData.TTSapiKey
elevenlabs.set_api_key(TTSapiKey)


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

def ttsElevenLabs(text):
    voice = elevenlabs.Voice(
        voice_id = "MBl73QmiIEX1OVzDjkjN",
        settings = elevenlabs.VoiceSettings(
            stability = 0,
            similarity_boost = 0.75
        )
    )

    audio = elevenlabs.generate(
        text= text,
        voice = voice
    )

    elevenlabs.play(audio)

if __name__ == "__main__":
    ttsPlay("Hello World!")
