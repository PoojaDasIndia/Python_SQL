import mysql.connector as con

try:
    # database k sath  connection
    mydb = con.connect(
        host='localhost',
        user='root',
        password='poojadas1993',
        database='EmployeeDetail',

    )
    print("Connection esatalised")

    query = "SELECT * FROM EmployeeDemo "
    # Extracting Table recorde    
    cur = mydb.cursor()
    cur.execute(query)

    # fetchall() used to  extract all recorded in from of list of tuples
    result = cur.fetchall()

    # print result which is list of Tuple conatin by the help of for loop
    for i in result:
        print(i)

    # fetchone()
    # result= cur.fetchone()
    # print(result)

    mydb.close()

except Exception as e:
    mydb.close()
    print(str(e))
