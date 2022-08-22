"""
Delete Collection
You can delete a table, or collection as it is called in MongoDB, by using the drop() method.

"""

import pymongo

# connection with mongoclient
myclient = pymongo.MongoClient("localhost", 27017)

# database created
mydb = myclient["EmployeeDetail"]

# create Collection or Table

mycoll = mydb['EmployeeDemo']

mycoll.drop()

"""
The drop() method returns true if the collection was dropped successfully, and false if the collection does not exist.

"""

for doc in mycoll.find():
    print(doc)
