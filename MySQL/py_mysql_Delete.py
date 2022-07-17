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

    # DELETE Table recorde    
    cur = mydb.cursor()
    # DELETE FROM EmployeeDemo delete all record
    # query = "DELETE FROM EmployeeDemo where Salary>600000"

    query = '''
                DELETE S1 FROM employeedemo AS S1  
                INNER JOIN employeedemo AS S2   
                WHERE S1.EmpID = S2.EmpID ; 
            '''
    cur.execute(query)

    # commit karna import h for permanently
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
