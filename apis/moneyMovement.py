import requests
import os
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Get the API keys from the environment variables
moneyMovementAPI = os.getenv('MONEY_MOVEMENT_API_KEY')
if not apiKey:
    raise ValueError('MONEY_MOVEMENT_API_KEY not found in environment variables')
else: 
    import requests
    
    API_URL = "https://alpha-api.usbank.com/innovation/bank-node/customer-accounts/v1/"
    API_KEY = "nPtN8LARVh1Q4b0GZKuFnsMATIc0TJet"
    API_SECRET = "20LxAZoBaJZjMkAI"
    
    def find_customer(customer_id):
        auth = (API_KEY, API_SECRET)
        
        headers = {
        "content-type": "application/json",
        "Accept": "application/json",
        }
        
        url = API_URL + "customer/" + customer_id + "/accounts"
        
        try:
            response = requests.get(url, auth=auth, headers=headers)
        
            print(response.status_code)
            print(response.json())
        except Exception as e:
            print(e)
    
    customer_id = "6763895841"
    find_customer(customer_id)

moneyMovementSecret = os.getenv('MONEY_MOVEMENT_API_SECRET')
if not apiKey:
    raise ValueError('MONEY_MOVEMENT_API_SECRET not found in environment variables')