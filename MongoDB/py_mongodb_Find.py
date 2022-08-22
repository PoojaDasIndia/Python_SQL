import pymongo

# connection with mongoclient
myclient = pymongo.MongoClient("localhost", 27017)

# database created
mydb = myclient["EmployeeDetail"]

# create Collection or Table

mycoll = mydb['EmployeeDemo']

""""In MongoDB we use the find and findOne methods to find data in a collection.

Just like the SELECT statement is used to find data in a table in a MySQL database."""

doc = mycoll.find_one()
print(doc)

"""No parameters in the find() method gives you the same result as SELECT * in MySQL."""

for doc in mycoll.find():
    print(doc)

"""Return Only Some Fields"""
for doc in mycoll.find({}, {"_id": 0, "name": 1, 'address': 1}):
    print(doc)
