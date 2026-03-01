from speech_to_text import speech_to_text
from dream_processor import dream_processor
from dream_interpretor import dream_interpretor
from image_generator import image_generator
from datetime import date

choix_mode= input()
speech = True if choix_mode == 1 else False

if speech:
    dream = speech_to_text()
else:
    dream = "je vole en battant des bras au dessus des pins"

processed_dream = dream_processor(dream)

interpretation = dream_interpretor(processed_dream)
image_path = image_generator(processed_dream)

dreams = open("data/dreams.json", "w+")
dreams.write("{"+f"\n\"date\": \"{date.today()}\",\n\"raw_text\": \"{dream}\",\n\"summary\": {processed_dream},\n\"interpretation\": \"{interpretation}\",\n\"image_path\": \"{image_path}\"\n"+"}")