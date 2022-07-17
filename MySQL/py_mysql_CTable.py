
import mysql.connector as con


#database k sath  connection
mydb=con.connect(
    host='localhost',
    user='root',
    password='poojadas1993',
    database='EmployeeDetail'
    )
query="CREATE TABLE EmployeeDemo(EmpID INT AUTO_INCREMENT PRIMARY KEY,FirstName varchar(50),LastName varchar(50),Age Integer(3),Salary Float(10,3))"
try:   
    #create table 
    cur=mydb.cursor()
    cur.execute(query)
    print("Table Created!!")
    mydb.close()
    
except Exception as e:
    mydb.close()
    print("TABLE  Already EXITED !!")
    print(str(e))    
 




