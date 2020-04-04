from flask import Flask, render_template, redirect, url_for, request, session, abort, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

from DataAccess.DBConnectionFood import insert_into_database

app = Flask(__name__)
app.secret_key = 'watermelonsugar'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'wasteless'

# Intialize MySQL
mysql = MySQL(app)

def add_item():
    msg = ''
    if request.method == 'POST' and 'name' in request.form and 'quantity' in request.form and 'calories' in request.form and 'expiredate' in request.form:
        name = request.form['name']
        quantity = request.form['quantity']
        calories = request.form['calories']
        expiredate = request.form['expiredate']
        insert_into_database(name, quantity, calories, expiredate)
        return render_template('welcome.html', msg=msg)
    return render_template('additem.html', msg=msg)