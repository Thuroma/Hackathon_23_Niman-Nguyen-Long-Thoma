from flask import Flask, render_template, request  # NOT the same as requests 

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run()