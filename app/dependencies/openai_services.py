import openai
from app.core.config import settings

def get_openai_client():
    return openai.OpenAI(api_key="***")  #