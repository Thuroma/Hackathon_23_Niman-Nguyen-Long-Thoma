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
    account_data = coreBanking.account_data()
    transaction_data = coreBanking.transaction_data()

    return render_template('homepage.html',
                            username=username,
                            account_data=account_data,
                            transaction_data=transaction_data
                            )

@app.route('/account_info')
def account_info_page():
    return render_template('account_info.html')

@app.route('/commitments')
def commitments_page():
    return render_template('commitments.html')

if __name__ == '__main__':
    app.run()