from pymongo import MongoClient

"""To create a database in MongoDB, start by creating a MongoClient object, then specify a connection URL with the correct ip address and 
the name of the database you want to create."""

myclient =MongoClient('localhost', 27017)


mydb=myclient['EmployeeDetail']



"""Important: In MongoDB, a database is not created until it gets content!

MongoDB waits until you have created a collection (table), with at least one document (record) before it actually creates the database (and collection)."""


# check if a database exist by listing all databases in you system

# Return a list of your system's databases
print(myclient.list_database_names())

# Check if "EmployeeDetail" exists

dblist=myclient.list_database_names()
if "EmployeeDetail" in dblist:
    print("The database Exits")
else:
    print("The database  not Exits")


