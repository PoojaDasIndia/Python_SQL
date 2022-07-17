import mysql.connector as con

#connection
mydb=con.connect(host='localhost',user='root',password='poojadas1993')

#crerating cursor object
#create a cursor to execute queries
cur=mydb.cursor()  #cur just object name

# Show databases;
cur.execute("SHOW DATABASES; ")
for i in cur:
    print(i)




