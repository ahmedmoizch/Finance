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
    'database': 'portfolio',
    'auth_plugin': 'mysql_native_password'
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('login_email')
        passw = request.form.get('login_password')

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        cursor.execute("select exists ( select 1 from users where email = (%s) AND pass = (%s) ) AS is_valid;", (username, passw))

        result = cursor.fetchone()
        is_valid = result[0]

        cursor.close()
        connection.close()

        if is_valid == 1:
            print("Login Successful")
            return redirect(url_for('home'))
        else:
            print("Login failed")

    return render_template('login.html')


@app.route('/psx', methods=['GET','POST'])
def psx():
    
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    cursor.execute('Select * from psx_cache')

    data = cursor.fetchall()
    heads = cursor.column_names

    connection.close()
    cursor.close()


    return render_template('psx.html', heads=heads, data=data)


@app.route('/commodity', methods=['GET','POST'])
def commodity():

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("select * from commodity_cache")


    heads = cursor.column_names
    data = cursor.fetchall()

    connection.close()
    cursor.close()

    return render_template('commodity.html', heads=heads, data=data)


@app.route('/crypto', methods=['GET','POST'])
def crypto():
    return render_template('crypto.html')


@app.route('/holdings', methods = ['GET','POST'])
def holdings():

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    if request.method == 'POST':
        category = request.form.get("asst_cat")
        asset_name = request.form.get("asset_name")
        asset_quantity = request.form.get("asset_quantity")
        asset_comission = request.form.get("asset_comission")
        asset_price = request.form.get("asset_price")

        # Hardcoded for now
        user: int = 1

        cursor.execute("INSERT INTO HOLDINGS (user_id, asset_symbol, asset_quantity, buy_price, comission) VALUES(%s,%s,%s,%s,%s)", (user,asset_name,asset_quantity,asset_price,asset_comission,))

        connection.commit()
        return redirect(url_for('holdings'))
        #print(category,asset_name,asset_quantity,asset_price,asset_comission)

    cursor.execute("SELECT holdings.asset_symbol, holdings.asset_quantity, holdings.buy_price, psx_cache.Current FROM holdings INNER JOIN psx_cache ON holdings.asset_symbol = psx_cache.symbol where holdings.user_id = 1;")
    heads = ["Symbol",	"Quantity",	"buying",	"Current", "PnL"]
    data = cursor.fetchall()

    cursor.close()
    connection.close()


    
    return render_template('holdings.html', heads=heads, data=data)


if __name__ == '__main__':
    app.run(debug=True)