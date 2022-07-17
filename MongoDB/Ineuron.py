from pymongo import MongoClient


client = MongoClient("mongodb+srv://Pooja:poojadas1993@clustertest.9obhy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

mydb=client['Mongotest']
coll = mydb['test']
d = {
    "name": "Riya",
    "email": "rama93@outlook.com",
    "surname": "Sharma"
}
coll.insert_one(d)
