import requests
import os
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Get the API keys from the environment variables
cardAsAServiceAPI = os.getenv('CARD_AS_A_SERVICE_API_KEY')
if not apiKey:
    raise ValueError('CARD_AS_A_SERVICE_API_KEY not found in environment variables')

cardAsAServiceSecret = os.getenv('CARD_AS_A_SERVICE_API_SECRET')
if not apiKey:
    raise ValueError('CARD_AS_A_SERVICE_API_SECRET not found in environment variables')