from flask import Flask, render_template, request  # NOT the same as requests 
from apis import coreBanking

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/homepage')
def homepage():
    account_info = coreBanking.get_customer_account_info()
    customer_info = coreBanking.get_customer_personal_info()

    
    return render_template('homepage.html',
                            account_info=account_info,
                            customer_info=customer_info,
                            )

@app.route('/account_info')
def account_info_page():
    return render_template('account_info.html')

@app.route('/commitments')
def commitments_page():
    return render_template('commitments.html')

if __name__ == '__main__':
    app.run()