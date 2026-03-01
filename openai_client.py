from openai import OpenAI

def openAI_client():
    api_key_file = open("api\open_ai_api_key.txt")
    client = OpenAI(api_key_file.read())
    api_key_file.close()
    return client
