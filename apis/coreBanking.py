import requests
import os
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Get the API keys from the environment variables
coreBankingAPI = os.getenv('CORE_BANKING_API_KEY')
if not apiKey:
    raise ValueError('CORE_BANKING_API_KEY not found in environment variables')
    
coreBankingSecret = os.getenv('CORE_BANKING_API_SECRET')
if not apiKey:
    raise ValueError('CORE_BANKING_API_SECRET not found in environment variables')    