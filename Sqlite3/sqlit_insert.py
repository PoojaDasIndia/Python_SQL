import sqlite3

con = sqlite3.connect("Student.db")  # connection has been created
print("Connection Established !! ")
try:
    n = int(input("Enter the number of record want to insert : "))
    for i in range(n):
        Name = input("Enter Name:")
        Roll = int(input("Enter Roll:"))
        Fee = int(input("Enter Fee:"))

        query = f"INSERT INTO StudentDetail VALUES ('{Name}','{Roll}',{Fee})"
        cur = con.cursor()

        cur.execute(query)
        con.commit()

        print(cur.rowcount, "Inserted")
    con.close()
    print(n, "Row Inserted")

except Exception as e:
    print(e)
