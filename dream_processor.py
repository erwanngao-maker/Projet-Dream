import os

from groq import Groq
from groq_client import groq_client as gc


def dream_processor(dream):
    
    client = gc()
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Analyse le reve : \"{dream}\" et structure-le en : \n- Personnages\n- Lieu\n- Émotions\n- Symboles importants\n- Résumé en 5 lignes\n. Je veux le resultat au format json",
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message
