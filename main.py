from flask import Flask
from flask import render_template

app = Flask(__name__)



@app.route('/')
def speak():
    return render_template('speak.html')


