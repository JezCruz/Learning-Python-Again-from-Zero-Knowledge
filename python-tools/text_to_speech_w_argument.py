import argparse
import pyttsx3

parser = argparse.ArgumentParser(description="Simple Text to Speech CLI")
parser.add_argument("text", help="Text to speak")
parser.add_argument("--rate", type=int, default=150, help="Speech rate")
args = parser.parse_args()

engine = pyttsx3.init()
engine.setProperty("rate", args.rate)
engine.say(args.text)
engine.runAndWait()