from pymongo import MongoClient


client = MongoClient("mongodb+srv://Pooja:poojadas1993@clustertest.9obhy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

mydb=client['Mongotest']
coll = mydb['test']
d = {
    "name": "Pooja",
    "email": "poojadas2004@outlook.com",
    "surname": "Das"
}
coll.insert_one(d)
