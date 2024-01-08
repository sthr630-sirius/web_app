import sqlite3

DATABASE = 'database.db'

def create_stocks_table():
    con = sqlite3.connect(DATABASE)
    con.execute('create table if not exists kitchen_stocks(id integer primary key autoincrement, item string, quantity integer, unit text)')
    con.execute('create table if not exists bathroom_stocks(id integer primary key autoincrement, item string, quantity integer, unit text)')
    con.execute('create table if not exists satohiro_stocks(id integer primary key autoincrement, item string, quantity integer, unit text)')
    con.close()