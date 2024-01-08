from flask import Flask
app = Flask(__name__)
import web_stocks.main

from web_stocks import db
db.create_stocks_table()