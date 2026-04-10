import argparse
import pyttsx3

parser = argparse.ArgumentParser(description="Simple Text to Speech CLI")
parser.add_argument("text", help="Text to speak")
args = parser.parse_args()

engine = pyttsx3.init()
engine.say(args.text)
engine.runAndWait()