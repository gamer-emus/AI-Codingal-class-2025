from googletrans import Translator
import speech_recognition as sr

translator = Translator()
recognizer = sr.Recognizer()


with sr.AudioFile("TTs_trail.wav") as source:
    audio = recognizer.record(source)

text = recognizer.recognize_google(audio)
print("You said:-", text)

translated = translator.translate(text, dest="fr")
print("Translated:-", translated.text)