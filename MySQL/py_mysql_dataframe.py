import mysql.connector as con
import pandas as pd
try:
    # database k sath  connection
    mydb = con.connect(
        host='localhost',
        user='root',
        password='poojadas1993',
        database='EmployeeDetail'
    )
    print(mydb.is_connected())

    query = "SELECT * FROM EmployeeDemo;"

    # print using pandas
    result_database = pd.read_sql(query, mydb)

    print(result_database)
    mydb.close()
    # data = pd.read_csv('mydata.csv')
    # print(data)

except Exception as e:
    mydb.close()
    print(str(e))
