
choix_mode= input()
speech = True if choix_mode == 1 else False

if speech:
    Dream = speech_to_text()
else:
    Dream = "je vole en battant des bras au dessus des pins"

