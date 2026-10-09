# Jarvis - Voice AI Assistant

A voice-controlled desktop assistant for macOS. Say "Jarvis" followed by a command, and it can open apps, close apps, and answer questions out loud.

## Features
- Wake word: say "Jarvis"
- Open and close Mac apps by voice ("Jarvis, open Safari")
- Answers questions using the OpenAI API
- Speaks replies out loud

## Tech Stack
Python, OpenAI API, SpeechRecognition

## Setup
1. Clone the repo and go into the folder
2. Install portaudio: `brew install portaudio`
3. Create a virtual environment:
```
   python3 -m venv venv
   source venv/bin/activate
```
4. Install packages: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and add your OpenAI API key
6. Run: `python main.py`

## Usage
- "Jarvis, open Safari"ß
- "Jarvis, close Safari"
- "Jarvis, what is Python?"
- "Jarvis, stop" to quit

## Notes
Speech recognition and AI answers need an internet connection. Only app control and text-to-speech run locally on your Mac.