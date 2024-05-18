from flask import Flask
app = Flask(__name__)

import love_mission.main

from love_mission import db
db.create_questions_table()