import os
from dotenv import load_dotenv
from flask import Flask, render_template, session, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = "$$"

session = {
    'user': 'root',
    'password': '123',
}


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if 'user' in session == 'root':
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

