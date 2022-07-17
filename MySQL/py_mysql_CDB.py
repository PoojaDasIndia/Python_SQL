import mysql.connector as con

# if database available this use   try -except
try:
    # connection
    mydb = con.connect(host='localhost', user='root', password='poojadas1993')

    # creating cursor object
    # create a cursor to execute queries
    cur = mydb.cursor()  # cur just object name

    # create database
    cur.execute("CREATE DATABASE EmployeeDetail")
    print("DATABASE Created!!")
    mydb.close()
# DROP DATABASE employeedemo

except Exception as e:
    mydb.close()
    print("DATABASE  Already EXITED !!")
    print(str(e))
