from pymongo import MongoClient

client = MongoClient("mongodb+srv://Pooja:poojadas1993@clustertest.9obhy.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# print(db)

database=client['Mongotest']
collection = database['test']
record = collection.find({'companyName': 'iNeuron'})
for i in record:
    print(i)