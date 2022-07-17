import mysql.connector as con

# database k sath  connection
mydb = con.connect(
    host='localhost',
    user='root',
    password='poojadas1993',
    database='EmployeeDetail'
)

# alter table
# query="ALTER TABLE employeedemo MODIFY  EmpID INT AUTO_INCREMENT PRIMARY KEY; "
query="DESC employeedemo ; "

cur = mydb.cursor()
cur.execute(query)