import pymongo

#connection with mongoclient
myclient=pymongo.MongoClient("localhost",27017)

#database created
mydb=myclient["EmployeeDetail"]

#create Collection or Table

mycoll=mydb['EmployeeDemo']

"""
Update Collection
You can update a record, or document as it is called in MongoDB, by using the update_one() method.

The first parameter of the update_one() method is a query object defining which document to update.
"""


myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycoll.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycoll.find():
  print(x)


myquery = {"address":{"$regex":"^S" }}
newvalues = { "$set": { "name": "Pooja" } }

mycoll.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycoll.find():
  print(x)  

myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycoll.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")  