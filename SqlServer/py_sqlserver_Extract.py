import pyodbc

"""The connection string
Use the pyodbc.drivers() method to find available drivers;
 the connection strings for these are essentially the same and will look like this:"""

# If you use SQL Server Authentication to connect to the server
try:
    mydb = pyodbc.connect(driver='{SQL Server Native Client 11.0}',
                          host=r'DODO-7\SQLEXPRESS',
                          UID='DODO-7',
                          PWD="poojadas123",
                          database="StudentDetail",
                          trusted_connection="yes")

    # If you use Windows Authentication to connect to the server
    print("CONNECTION ESTABLISHED!!")

    n = int(input("Enter the number of record want to insert : "))

    query = "SELECT * FROM Student"

    # Insert table
    cur = mydb.cursor()
    c = cur.execute(query)

    for i in c:  # cur.fetchall():
        print(i)

    mydb.close()
except Exception as e:
    mydb.close()
    print("TABLE  Already EXITED !!")
    print(str(e))
