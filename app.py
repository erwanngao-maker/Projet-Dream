from speech_to_text import speech_to_text
from dream_processor import dream_processor

choix_mode= input()
speech = True if choix_mode == 1 else False

if speech:
    dream = speech_to_text()
else:
    dream = "je vole en battant des bras au dessus des pins"

processed_dream = dream_processor(dream)