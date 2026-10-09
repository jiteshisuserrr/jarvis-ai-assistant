import os
import subprocess
import speech_recognition as sr
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

recognizer = sr.Recognizer()
mic = sr.Microphone()

WAKE = "jarvis"

def ask_ai(text):
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Jarvis, a helpful assistant. Answer in 1-2 short sentences."},
            {"role": "user", "content": text},
        ],
    )
    return r.choices[0].message.content

def handle_command(text):
    t = text.lower()
    if t.startswith("open "):
        app = text[5:].strip()
        os.system(f'open -a "{app}"')
        return f"Opening {app}"
    if t.startswith("close "):
        app = text[6:].strip()
        os.system(f'osascript -e \'quit app "{app}"\'')
        return f"Closing {app}"
    return None

def speak(text):
    print("Jarvis:", text)
    subprocess.run(["say", text])

def listen():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            return ""
    try:
        return recognizer.recognize_google(audio).lower()
    except (sr.UnknownValueError, sr.RequestError):
        return ""

speak("Say Jarvis to wake me up")

while True:
    heard = listen()
    if heard:
        print("Heard:", heard)
    if WAKE in heard:
        command = heard.split(WAKE, 1)[1].strip()
        if not command:
            speak("Yes?")
            command = listen()
        if command in ("exit", "quit", "stop"):
            speak("Goodbye")
            break
        speak(handle_command(command) or ask_ai(command))