"""A collection in MongoDB is the same as a table in SQL databases."""

import pymongo

# connection with mongoclient
myclient = pymongo.MongoClient("localhost", 27017)

# database created
mydb = myclient["EmployeeDetail"]

# create Collection or Table

mycoll = mydb['EmployeeDemo']

# You can check if a collection exist in a database by listing all collections:

print(mydb.list_collection_names())

# Check if the "customers" collection exists:

collist = mydb.list_collection_names()

if "EmployeeDemo" in collist:
    print("The collection Exit")
else:
    print("The collection  not Exit")
