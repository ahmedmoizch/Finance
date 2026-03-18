import os
from dotenv import load_dotenv
from flask import Flask, render_template, session, request, redirect, url_for
import mysql.connector
import pandas as pd

app = Flask(__name__)
app.secret_key = "$$"

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345678',
    'database': 'portfolio'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('login_email')
        passw = request.form.get('login_password')

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        cursor.execute("select exists ( select 1 from user_login where email = (%s) AND pass = (%s) ) AS is_valid;", (username, passw))

        result = cursor.fetchone()
        is_valid = result[0]

        cursor.close()
        connection.close()

        if is_valid == 1:
            return redirect(url_for('home'))
        else:
            print("Login failed")

    return render_template('login.html')



@app.route('/psx', methods=['GET','POST'])
def psx():

    df = pd.read_csv('psx_cache.csv')
    selected_col = ['SYMBOL', 'CURRENT','HIGH','LOW', 'VOLUME']

    df = df[selected_col]

    heads = df.columns
    data = df.values


    return render_template('psx.html', heads=heads, data=data)


if __name__ == '__main__':
    app.run(debug=True)
