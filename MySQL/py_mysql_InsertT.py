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
    # n times insert happen
    n = int(input("Enter the number of record want to insert : "))
    for i in range(n):
        Employee_Id = int(input("Enter Employee ID:"))
        firstname = input("Enter First name:")
        lastname = input("Enter Last Name:")
        Age = int(input("Enter Age:"))
        Department = input("Enter Department:")
        Salary = float(input("Enter Salary:"))

        # insert function (EmpID,FirstName,LastName,Age,Department,Salary)

        query = f"INSERT INTO employeedemo VALUES ({Employee_Id},'{firstname}','{lastname}',{Age},'{Department}',{Salary})"

        # Insert table    
        cur = mydb.cursor()
        cur.execute(query)
        # query""INSERT INTO employeedemo (EmpID,FirstName) VALUES (%s,%s)
        # execute many if  we pass list of tuple l=[(),(),()]
        # cur.executemany(query,l)  

        mydb.commit()
        print(f"{cur.rowcount} Values inserted into the table!!")
    print(f"{n} Values inserted into the table!!")
    print(cur.lastrowid)
    mydb.close()


except Exception as e:
    mydb.close()
    print(str(e))
