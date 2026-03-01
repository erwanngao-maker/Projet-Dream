from groq_client import groq_client as gc
def dream_interpretor(dream):
    
    client = gc()
    prompt_txt = open("prompts/summary_prompt.txt")
    line = prompt_txt.read()
    prompt = ''

    while line != '':
        prompt += line
        line = prompt_txt.read()
    prompt_txt.close()
    prompt.replace("_", dream)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message