import sqlite3

DATABASE = "./love_mission/database.db"

def create_questions_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS questions (no, content)")
    con.close()