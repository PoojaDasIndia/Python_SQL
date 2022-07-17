import sqlite3

con = sqlite3.connect("Student.db")  # connection has been created
print("Connection Established !! ")
try:

    query = "Select * from StudentDetail;"
    cur = con.cursor()
    cur.execute(query)
    # con.commit()
    print(cur.fetchone())
    print("*********************")
    for i in cur.fetchall():
        print(i)
    print("*********************")
    for i in cur.fetchall():
        print(i)

    con.close()


except Exception as e:
    print(e)
