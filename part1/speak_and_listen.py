import pyttsx3
import speech_recognition as sr
import re

r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("voice", "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-ES_HELENA_11.0")


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)
        try:
            audio = r.recognize_google(audio, language="es-ES")
            audio = audio.replace(",", ".")
            return audio
        except sr.UnknownValueError:
            return


if __name__ == "__main__":
    speak("Probando si funciona todo")
    print(listen())

