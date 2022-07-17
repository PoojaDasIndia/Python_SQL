import mysql.connector as con

try:
    # database k sath  connection
    mydb = con.connect(
        host='localhost',
        user='root',
        password='poojadas1993',
        database='EmployeeDetail'
    )
    print(mydb.is_connected())

    # Update Table recorde    
    cur = mydb.cursor()

    query = "UPDATE EmployeeDemo SET Salary=Salary+5000 WHERE Salary<50000 "
    cur.execute(query)

    # commit karna import h
    mydb.commit()

    query = "SELECT * FROM EmployeeDemo "
    # Extracting Table recorde    
    cur.execute(query)

    # fetchall() used to  extract all recored in from of list of tuples
    result = cur.fetchall()

    # print result which is list of Tuple conatin by the help of for loop
    for i in result:
        print(i)

    mydb.close()

except Exception as e:
    mydb.close()
    print(str(e))
