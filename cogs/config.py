from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GOOGLE_API_KEY = os.getenv("google_api_key")
OPENAI_API_KEY = os.getenv("openai.api_key")
