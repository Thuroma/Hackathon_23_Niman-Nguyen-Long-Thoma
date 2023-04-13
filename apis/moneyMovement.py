import requests
import os
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Get the API keys from the environment variables
moneyMovementAPI = os.getenv('MONEY_MOVEMENT_API_KEY')
if not apiKey:
    raise ValueError('MONEY_MOVEMENT_API_KEY not found in environment variables')

moneyMovementSecret = os.getenv('MONEY_MOVEMENT_API_SECRET')
if not apiKey:
    raise ValueError('MONEY_MOVEMENT_API_SECRET not found in environment variables')