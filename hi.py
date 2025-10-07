import pyttsx3
import shutil
import os
import tempfile

def reset_win32com_cache():
    tmp = os.path.join(tempfile.gettempdir(), 'gen_py')
    if os.path.isdir(tmp):
        shutil.rmtree(tmp)

def speak(text):
    reset_win32com_cache()
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 140)
    engine.setProperty('volume', 0.9)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

print("Robo speaker ready! Type something (or 'exit'):")
while True:
    txt = input("You: ").strip()
    if txt.lower() == 'exit':
        speak("Goodbye!")
        break
    speak(txt)