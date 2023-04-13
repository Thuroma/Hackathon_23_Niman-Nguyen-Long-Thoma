from flask import Flask, render_template, request  # NOT the same as requests 

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/account_info')
def account_info_page():
    return render_template('account_info.html')

@app.route('/commitments')
def commitments_page():
    return render_template('commitments.html')

if __name__ == '__main__':
    app.run()