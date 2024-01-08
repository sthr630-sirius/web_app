'''       for local server     '''
from web_stocks import app
'''-------------------------'''
from flask import render_template, request, redirect
import sqlite3
DATABASE = 'database.db'

'''       for xserver       '''
#from flask import Flask
#app = Flask(__name__)
#import db
#db.create_stocks_table()
'''-------------------------'''

@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_kitchen_stocks = con.execute('SELECT * FROM kitchen_stocks').fetchall()
    db_bathroom_stocks = con.execute('SELECT * FROM bathroom_stocks').fetchall()
    db_satohiro_stocks = con.execute('SELECT * FROM satohiro_stocks').fetchall()
    con.close()

    kitchen_stocks = []
    bathroom_stocks = []
    satohiro_stocks = []
    for row in db_kitchen_stocks:
        kitchen_stocks.append({'id':row[0], 'item':row[1], 'quantity':row[2], 'unit':row[3]})
    for row in db_bathroom_stocks:
        bathroom_stocks.append({'id':row[0], 'item':row[1], 'quantity':row[2], 'unit':row[3]})
    for row in db_satohiro_stocks:
        satohiro_stocks.append({'id':row[0], 'item':row[1], 'quantity':row[2], 'unit':row[3]})
    return render_template(
        'index.html',
        kitchen_stocks=kitchen_stocks,
        bathroom_stocks=bathroom_stocks,
        satohiro_stocks=satohiro_stocks
    )

#---insert stock---#
@app.route("/insert_form/<table_name>")
def insert_form(table_name):
    title = '在庫登録'
    submit_value = '登録'
    form_action='insert_conf'
    return render_template(
        'form.html',
        form_action=form_action,
        submit_value=submit_value,
        title=title,
        table_name=table_name,
    )

@app.route("/insert_conf", methods=['POST'])
def insert_conf():
    table_name = request.form['table_name']
    item = request.form['item']
    quantity = request.form['quantity']
    unit = request.form['unit']
    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO %s ("item", quantity, "unit") VALUES(?, ?, ?)' %table_name, (item, quantity, unit))
    con.commit()
    con.close()
    return redirect("/")

#---update stock---#
@app.route("/update_form/<id>&<table_name>")
def update_form(id, table_name):
    title = '在庫更新フォーム'
    submit_value = '更新'
    form_action = 'update_conf'
    con = sqlite3.connect(DATABASE)
    data = con.execute('SELECT * FROM %s WHERE id=?' %table_name, (id,)).fetchall()
    con.close()
    item = data[0][1]
    unit = data[0][3]
    return render_template(
        'update_form.html',
        title=title,
        submit_value=submit_value,
        form_action=form_action,
        table_name=table_name,
        id=id,
        item=item,
        unit=unit
    )

@app.route("/update_conf", methods=['POST'])
def update_conf():
    table_name = request.form['table_name']
    id = request.form['id']
    delta = request.form['delta']
    con = sqlite3.connect(DATABASE)
    quantity = con.execute('SELECT quantity FROM %s WHERE id=?' %table_name, (id,)).fetchone()[0]
    quantity = quantity + int(delta)
    con.execute('UPDATE %s SET quantity=? WHERE id=?' %table_name, (quantity, id))
    con.commit()
    con.close()
    return redirect("/")

#---delete from---#
@app.route("/delete_form/<id>&<table_name>")
def delete_form(id, table_name):
    title = '在庫削除フォーム'
    submit_value = '削除'
    form_action = 'delete_conf'
    con = sqlite3.connect(DATABASE)
    data = con.execute('SELECT * FROM %s WHERE id=?' %table_name, (id,)).fetchall()
    con.close()
    item = data[0][1]
    quantity = data[0][2]
    unit = data[0][3]
    return render_template(
        'delete_form.html',
        title=title,
        submit_value=submit_value,
        form_action=form_action,
        table_name=table_name,
        id=id,
        item=item,
        quantity=quantity,
        unit=unit
    )

@app.route("/delete_conf", methods=['POST'])
def delete_conf():
    table_name = request.form['table_name']
    id = request.form['id']
    con = sqlite3.connect(DATABASE)
    con.execute('DELETE FROM %s WHERE id=?' %table_name, (id,))
    con.commit()
    con.close()
    return redirect("/")