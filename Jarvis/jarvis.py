import datetime
import os
import random
import subprocess
import sys
import webbrowser as wb
from pathlib import Path

import pyjokes
import pyautogui
import pyttsx3
import speech_recognition as sr
import wikipedia

# BASIC LANGUAGE STRINGS
STRINGS = {
    'fr': {
        'welcome': "Bon retour, monsieur !",
        'morning': "Bon matin !",
        'afternoon': "Bon après-midi !",
        'evening': "Bonsoir !",
        'night': "Bonne nuit, à demain.",
        'service': "{} à votre service. Comment puis-je vous aider ?",
        'time': "L'heure actuelle est ",
        'date': "La date d'aujourd'hui est le ",
        'screenshot': "Capture d'écran sauvegardée sous {}.",
        'listening': "À l'écoute...",
        'recognizing': "Reconnaissance...",
        'error_music': "Répertoire Musique introuvable.",
        'playing': "Lecture de {}.",
        'no_song': "Aucun morceau trouvé.",
        'ask_name': "Comment souhaitez-vous m'appeler ?",
        'name_set': "Très bien, je m'appellerai {} à partir de maintenant.",
        'wiki_search': "Recherche sur Wikipedia...",
        'no_result': "Je n'ai rien trouvé.",
        'shutdown': "Extinction du système !",
        'restart': "Redémarrage du système !",
        'offline': "Je passe en mode hors ligne. Bonne journée !"
    },
    'en': {
        'welcome': "Welcome back, sir!",
        'morning': "Good morning!",
        'afternoon': "Good afternoon!",
        'evening': "Good evening!",
        'night': "Good night, see you tomorrow.",
        'service': "{} at your service. How may I assist you?",
        'time': "The current time is ",
        'date': "The current date is ",
        'screenshot': "Screenshot saved as {}.",
        'listening': "Listening...",
        'recognizing': "Recognizing...",
        'error_music': "Music directory not found.",
        'playing': "Playing {}.",
        'no_song': "No song found.",
        'ask_name': "What would you like to name me?",
        'name_set': "Alright, I will be called {} from now on.",
        'wiki_search': "Searching Wikipedia...",
        'no_result': "I couldn't find anything.",
        'shutdown': "Shutting down system!",
        'restart': "Restarting system!",
        'offline': "Going offline. Have a good day!"
    }
}

# INIT
engine = pyttsx3.init()
voices = engine.getProperty('voices')
VOICE_MAP = {'fr': None, 'en': None}

for voice in voices:
    v_lang = str(voice.languages).lower()
    if "fr-fr" in v_lang or "french" in voice.name.lower():
        VOICE_MAP['fr'] = voice.id
    if "en-us" in v_lang or "english" in voice.name.lower():
        VOICE_MAP['en'] = voice.id

def set_voice(lang):
    if VOICE_MAP.get(lang):
        engine.setProperty('voice', VOICE_MAP[lang])

engine.setProperty('rate', 170)
engine.setProperty('volume', 1)

# CORE FUNCTIONS
def speak(text, lang='en'):
    set_voice(lang)
    engine.say(text)
    engine.runAndWait()
