import pymongo

# connection with mongoclient
myclient = pymongo.MongoClient("localhost", 27017)

# database created
mydb = myclient["EmployeeDetail"]

# create Collection or Table

mycoll = mydb['EmployeeDemo']

"""To delete one document, we use the delete_one() method.

The first parameter of the delete_one() method is a query object defining which document to delete.

Note: If the query finds more than one document, only the first occurrence is deleted."""

myquery = {"address": "Mountain 21"}

x = mycoll.delete_one(myquery)

print(x.deleted_count, " documents deleted.")

myquery = {"address": {"$regex": "^S"}}

x = mycoll.delete_many(myquery)

print(x.deleted_count, " documents deleted.")

myquery = {"Class": "MCA"}

x = mycoll.delete_many(myquery)

print(x.deleted_count, " documents deleted.")

# find()
for doc in mycoll.find():
    print(doc)

"""Delete All Documents in a Collection
To delete all documents in a collection, pass an empty query object to the delete_many() method:"""

x = mycoll.delete_many({})

print(x.deleted_count, " documents deleted.")
# find()
for doc in mycoll.find():
    print(doc)
