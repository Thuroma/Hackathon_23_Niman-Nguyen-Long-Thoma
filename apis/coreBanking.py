import requests
import os
from pprint import pprint
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Get the API keys from the environment variables
API_KEY = os.getenv('US_BANKING_API_KEY')
if not API_KEY:
    raise ValueError('US_BANKING_API_KEY not found in environment variables')

API_SECRET = os.getenv('US_BANKING_SECRET_KEY')
if not API_SECRET:
    raise ValueError('US_BANKING_SECRET_KEY not found in environment variables')

def get_customer_account_info():

    try:
        API_URL = "https://alpha-api.usbank.com/innovation/bank-node/customer-accounts/v1/"
        customer_id = "6763895841"
        auth = (API_KEY, API_SECRET)

        headers = {
        "content-type": "application/json",
        "Accept": "application/json",
        }

        url = API_URL + "customer/" + customer_id + "/accounts"
        response = requests.get(url, auth=auth, headers=headers)
        account_data = response.json()
        accounts = account_data['accounts']

        return accounts

    except Exception as e:
        print(e)


def get_customer_personal_info():

    try:
        API_URL = "https://alpha-api.usbank.com/innovation/bank-node/customer-accounts/v1/"
        customer_id = "6763895841"
        auth = (API_KEY, API_SECRET)

        headers = {
        "content-type": "application/json",
        "Accept": "application/json",
        }

        url = API_URL + "customer/" + customer_id
        response = requests.get(url, auth=auth, headers=headers)
        account_data = response.json()
        customers = account_data['customer']

        return customers

    except Exception as e:
        print(e)


get_customer_account_info()
get_customer_personal_info()