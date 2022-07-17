import pymongo

#connection with mongoclient
myclient=pymongo.MongoClient("localhost",27017)

#database created
mydb=myclient["EmployeeDetail"]

#create Collection or Table

mycoll=mydb['EmployeeDemo']

mydoc = mycoll.find().sort("name")

"""sort("name", 1) #ascending
sort("name", -1) #descending"""

for x in mydoc:
  print(x)
