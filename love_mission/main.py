from love_mission import app
from flask import render_template
import sqlite3
import random

DATABASE = "./love_mission/database.db"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_question")
def GetQuestion():
    return render_template('get_question.html')

@app.route("/print_question")
def PrintQuestion():
    con = sqlite3.connect(DATABASE)
    db_questions = con.execute("SELECT * FROM questions").fetchall()
    con.close()

    out_question = []

    n = len(db_questions)
    out_question_no = random.randint(0, n)
    out_question = db_questions[out_question_no][1]
    #for row in db_questions:
    #    questions.append({"no": row[0], "content": row[1]})

    return render_template(
        'print_question.html',
        question=out_question
    )
