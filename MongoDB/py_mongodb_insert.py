#A document in MongoDB is the same as a record in SQL databases.

"""To insert a record, or document as it is called in MongoDB, into a collection, we use the insert_one() method.

The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each field in the document you want to insert."""


import pymongo

#connection with mongoclient
myclient=pymongo.MongoClient("localhost",27017)

#database created
mydb=myclient["EmployeeDetail"]

#create Collection or Table

mycoll=mydb['EmployeeDemo']

# insert dictionary(document)
mydict={"Name":"Pooja","Class":"MCA"}


# Insert  document into collection/table
doc=mycoll.insert_one(mydict)  #insert_one() func hai


"""The insert_one() method returns a InsertOneResult object, which has a property, inserted_id,
 that holds the id of the inserted document."""
 
print(doc.inserted_id) # inserted_id function nhi h

"""Insert Multiple Documents"""

# To insert multiple documents into a collection in MongoDB, we use the insert_many() method.

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

doc=mycoll.insert_many(mylist)

print(doc.inserted_ids)  # now we used inseted_ids 

