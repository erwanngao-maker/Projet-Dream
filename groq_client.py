from groq import Groq

def groq_client():
    api_key_file = open("api\groq_api_key.txt")

    client = Groq(
            api_key= api_key_file.read()
        )
    return client