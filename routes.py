from flask import Blueprint, render_template
from app import mysql

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/productos')
def productos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM productos")
    productos = cur.fetchall()
    return render_template('productos.html', productos=productos)
