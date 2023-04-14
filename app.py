from flask import Flask, render_template, request  # NOT the same as requests 
from apis import coreBanking
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/homepage')
def homepage():
    username = request.args.get('username')

    # Account info data
    # account_data = coreBanking.get_customer_account_info()
    account_data = [
        {
        'description': 'Checkings Account 1010',
        'accountType': 'DEB',
        'availableBalance': '9000'
        },
        {
        'description': 'Checkings Account 4320',
        'accountType': 'DEB',
        'availableBalance': '4500'
        },
        {
        'description': 'Savings Account',
        'accountType': 'SAV',
        'availableBalance': '7000'
        },
        {
        'description': 'Credit Card Account',
        'accountType': 'CRE',
        'availableBalance': '3000'
        },

    ]

    return render_template('homepage.html',
                            username=username,
                            account_data=account_data
                            )

@app.route('/account_info')
def account_info_page():
    return render_template('account_info.html')

@app.route('/commitments')
def commitments_page():
    return render_template('commitments.html')

if __name__ == '__main__':
    app.run()