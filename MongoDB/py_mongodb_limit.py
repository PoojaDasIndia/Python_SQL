import pymongo

# connection with mongoclient
myclient = pymongo.MongoClient("localhost", 27017)

# database created
mydb = myclient["EmployeeDetail"]

# create Collection or Table

mycoll = mydb['EmployeeDemo']

for doc in mycoll.find().limit(5):
    print(doc)

for doc in mycoll.find().limit(-3):
    print(doc)
