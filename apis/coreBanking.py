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



def account_data():
    account_data = [
        {
        'description': 'Checkings Account 1010',
        'accountType': 'DEB',
        'availableBalance': '9000',
        'standing': '1.1'
        },
        {
        'description': 'Checkings Account 4320',
        'accountType': 'DEB',
        'availableBalance': '4500',
        'standing': '1.3'
        },
        {
        'description': 'Savings Account',
        'accountType': 'SAV',
        'availableBalance': '7000',
        'standing': '2.2'
        },
        {
        'description': 'Credit Card Account',
        'accountType': 'CRE',
        'availableBalance': '3000',
        'standing': '2.4'
        },
    ]

    return account_data



def transaction_data():
    tran = [
   {
       "accountID": "930516287777",
       "transactionID": "437740791403",
       "cardNumber": "",
       "maskedCardNumber": "",
       "referenceTransactionID": "",
       "postedTimestamp": "2021-08-13T01:26:35.000Z",
       "transactionTimestamp": "2021-08-13T01:26:35.000Z",
       "channel": "Check",
       "description": "Check",
       "memo": "",
       "debitCreditMemo": "DEBIT",
       "category": "",
       "subCategory": "",
       "reference": "",
       "status": "POSTED",
       "amount": "64",
       "payee": "Miller, Little and Rodriguez",
       "checkNumber": "1152",
       "foreignAmount": "0",
       "foreignCurrency": "",
       "transactionType": "CHECK",
   },
   {
       "accountID": "930516287777",
       "transactionID": "437740791402",
       "cardNumber": "",
       "maskedCardNumber": "",
       "referenceTransactionID": "",
       "postedTimestamp": "2021-08-02T03:24:16.000Z",
       "transactionTimestamp": "2021-08-02T03:24:16.000Z",
       "channel": "Electronic payment",
       "description": "Deposit",
       "memo": "",
       "debitCreditMemo": "CREDIT",
       "category": "",
       "subCategory": "",
       "reference": "Nader, Langosh and Morissette",
       "status": "POSTED",
       "amount": "639",
       "payee": "",
       "checkNumber": "",
       "foreignAmount": "0",
       "foreignCurrency": "",
       "transactionType": "DEPOSIT",
   },
   {
       "accountID": "930516287777",
       "transactionID": "437740791401",
       "cardNumber": "",
       "maskedCardNumber": "",
       "referenceTransactionID": "",
       "postedTimestamp": "2021-07-27T08:55:56.000Z",
       "transactionTimestamp": "2021-07-27T08:55:56.000Z",
       "channel": "Check",
       "description": "Deposit",
       "memo": "Check - 1242",
       "debitCreditMemo": "CREDIT",
       "category": "",
       "subCategory": "",
       "reference": "Kuphal, Torp and Bins",
       "status": "POSTED",
       "amount": "76",
       "payee": "",
       "checkNumber": "",
       "foreignAmount": "0",
       "foreignCurrency": "",
       "transactionType": "DEPOSIT",
   },
   {
       "accountID": "930516287777",
       "transactionID": "437740791400",
       "cardNumber": "",
       "maskedCardNumber": "",
       "referenceTransactionID": "",
       "postedTimestamp": "2021-07-18T06:58:37.000Z",
       "transactionTimestamp": "2021-07-18T06:58:37.000Z",
       "channel": "Check",
       "description": "Check",
       "memo": "",
       "debitCreditMemo": "DEBIT",
       "category": "",
       "subCategory": "",
       "reference": "",
       "status": "POSTED",
       "amount": "216",
       "payee": "Abernathy-Murray",
       "checkNumber": "1151",
       "foreignAmount": "0",
       "foreignCurrency": "",
       "transactionType": "CHECK",
   },
   {
       "accountID": "930516287777",
       "transactionID": "437740791399",
       "cardNumber": "",
       "maskedCardNumber": "",
       "referenceTransactionID": "",
       "postedTimestamp": "2021-07-08T11:20:28.000Z",
       "transactionTimestamp": "2021-07-08T11:20:28.000Z",
       "channel": "Electronic payment",
       "description": "Deposit",
       "memo": "",
       "debitCreditMemo": "CREDIT",
       "category": "",
       "subCategory": "",
       "reference": "Watsica-Grant",
       "status": "POSTED",
       "amount": "326",
       "payee": "",
       "checkNumber": "",
       "foreignAmount": "0",
       "foreignCurrency": "",
       "transactionType": "DEPOSIT",
   },
   {
       "accountID": "930516287777",
       "transactionID": "437740791398",
       "cardNumber": "",
       "maskedCardNumber": "",
       "referenceTransactionID": "",
       "postedTimestamp": "2021-07-03T14:20:15.000Z",
       "transactionTimestamp": "2021-07-03T14:20:15.000Z",
       "channel": "Electronic payment",
       "description": "Deposit",
       "memo": "",
       "debitCreditMemo": "CREDIT",
       "category": "",
       "subCategory": "",
       "reference": "Lockman Group",
       "status": "POSTED",
       "amount": "617",
       "payee": "",
       "checkNumber": "",
       "foreignAmount": "0",
       "foreignCurrency": "",
       "transactionType": "DEPOSIT",
   },
   {
       "accountID": "930516287777",
       "transactionID": "437740791397",
       "cardNumber": "",
       "maskedCardNumber": "",
       "referenceTransactionID": "",
       "postedTimestamp": "2021-06-09T04:31:17.000Z",
       "transactionTimestamp": "2021-06-09T04:31:17.000Z",
       "channel": "Check",
       "description": "Check",
       "memo": "",
       "debitCreditMemo": "DEBIT",
       "category": "",
       "subCategory": "",
       "reference": "",
       "status": "POSTED",
       "amount": "129",
       "payee": "Morissette-Graham",
       "checkNumber": "1150",
       "foreignAmount": "0",
       "foreignCurrency": "",
       "transactionType": "CHECK",
       },
   ]

    return tran


    






get_customer_account_info()
get_customer_personal_info()