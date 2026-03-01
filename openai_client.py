from openai import OpenAI

def openAI_client():
    api_key_file = open("api/open_ai_key.txt")
    api_key = api_key_file.read()
    client = OpenAI(api_key=api_key)
    api_key_file.close()
    return client
