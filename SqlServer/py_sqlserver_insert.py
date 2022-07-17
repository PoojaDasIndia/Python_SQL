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

    n = int(input("Enter the number of record want to insert : "))
    for i in range(n):
        Roll_no = int(input("Enter Roll No.:"))
        Name = input("Enter Name:")
        Class = input("Enter Class:")
        Fee = int(input("Enter Fee:"))

        # insert function (EmpID,FirstName,LastName,Age,Department,Salary)

        query = f"INSERT INTO Student VALUES ({Roll_no},'{Name}','{Class}',{Fee})"

        # Insert table
        cur = mydb.cursor()
        cur.execute(query)

        print(f"{i + 1} Values inserted into the table!!")
        mydb.commit()

    mydb.close()
except Exception as e:
    mydb.close()
    print("TABLE  Already EXITED !!")
    print(str(e))
