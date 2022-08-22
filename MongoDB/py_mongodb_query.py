import pymongo

# connection with mongoclient
myclient = pymongo.MongoClient("localhost", 27017)

# database created
mydb = myclient["EmployeeDetail"]

# create Collection or Table

mycoll = mydb['EmployeeDemo']

myquery = {"address": "Park Lane 38"}

doc = mycoll.find(myquery)

for x in doc:
    print(x)

# Advanced Query
myquery1 = {"address": {"$gt": "S"}}
doc = mycoll.find(myquery1)

for x in doc:
    print(x)

"""E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetically),
 use the greater than modifier: {"$gt": "S"}:"""

# Filter With Regular Expressions

"""Regular expressions can only be used to query strings."""
"""To find only the documents where the "address" field starts with the letter "S", use the regular expression {"$regex": "^S"}:"""

myquery = {"address": {"$regex": "^S"}}

mydoc = mycoll.find(myquery)

for x in mydoc:
    print(x)
