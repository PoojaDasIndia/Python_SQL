import pyodbc

"""The connection string
Use the pyodbc.drivers() method to find available drivers;
 the connection strings for these are essentially the same and will look like this:"""

# If you use SQL Server Authentication to connect to the server
try:
    mydb = pyodbc.connect(driver='{SQL Server}',
                          host=r'DODO-7\SQLEXPRESS',
                          UID='DODO-7',
                          PWD="poojadas123",
                          database="StudentDetail",
                          trusted_connection="yes")

    # If you use Windows Authentication to connect to the server
    print("CONNECTION ESTABLISHED!!")

    cur = mydb.cursor()

    query = """CREATE TABLE Student
                (
                    Roll_No int,
                    Name varchar(50),
                    Class varchar(50),
                    Fee int
                )
        """

    cur.execute(query)
    cur.commit()  # commit  important in  sql server

    print("Table Created!!")
    mydb.close()

except Exception as e:
    mydb.close()
    print("TABLE  Already EXITED !!")
    print(str(e))
