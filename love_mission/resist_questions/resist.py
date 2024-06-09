import sqlite3

DATABASE = "../database.db"
con = sqlite3.connect(DATABASE)
con.execute("create table if not exists questions (no, content)")

n = 14
for i in range(n):
    q_no, question = input().split()
    con.execute("insert into questions values(?,?)", [q_no, question])
    print(f"no: {q_no} question: {question}")
    print("question: ", question)

con.commit()
con.close()
