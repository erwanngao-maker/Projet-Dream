from openai_client import openAI_client as oac
import base64
import os
from datetime import date
def image_generator(dream):
    
    client = oac()
    prompt_txt = open("prompts/image_prompt.txt")
    line = prompt_txt.read()
    prompt = ''
    while line != '':
        prompt += line
        line = prompt_txt.read()
    prompt_txt.close()
    prompt.replace("_", dream)
    
    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )
    image_base64 = result.data[0].b64_json
    file_path = os.path.join("data/images", f"reve_{date.today()}.png")
    with open(file_path, "wb") as f:
        f.write(base64.b64decode(image_base64))
    return file_path