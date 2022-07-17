import sqlite3
con = sqlite3.connect("Student.db")  # connection has been created
print("Connection Established !! ")
try:
    cur =con.cursor()
    # type of datatypes in sqlite
    # NULL,INTEGER,REAL,TEXT,BLOB
    query=""" CREATE TABLE StudentDetail(
    Name text, Roll integer, fee integer
    )
    """  # Table create
    cur.execute(query)
    con.commit()
    con.close()


except Exception as e:
    print(e)

