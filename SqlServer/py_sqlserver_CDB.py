import pyodbc

"""The connection string
Use the pyodbc.drivers() method to find available drivers;
 the connection strings for these are essentially the same and will look like this:"""

# If you use SQL Server Authentication to connect to the server
try:
    mydb = pyodbc.connect(driver='{SQL Server};',
                          host=r'DODO-7\SQLEXPRESS',
                          UID='DODO-7',
                          PWD="poojadas123",
                          database="Master",
                          trusted_connection="yes",
                          autocommit='YES')  # for create database use autocommit='yes'

    # If you use Windows Authentication to connect to the server just remove UID and PWD

    print("CONNECTION ESTABLISHED!!")  # print is connection established

    # create a cursor to execute queries
    cur = mydb.cursor()

    # create Database
    query = "CREATE DATABASE StudentDetail1"
    cur.execute(query)

    # print that Database
    print("Database Created!!")
    mydb.close()


except Exception as e:
    mydb.close()
    print("DATABASE  Already EXITED !!")
    print(str(e))
