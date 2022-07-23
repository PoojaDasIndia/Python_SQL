from pymongo import MongoClient

client = MongoClient("mongodb+srv://Pooja:poojadas1993@clustertest.9obhy.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# print(db)

database=client['Mongotest']
collection = database['NewTable']
# record = collection.find({'companyName': 'iNeuron'})
# record = collection.find({'courseOffered': {'$gt':'E'}})
#
# for i in record:
#     print(i)
# data =  [
#         {
#             "item": "canvas",
#             "qty": 100,
#             "size": {"h": 28, "w": 35.5, "uom": "cm"},
#             "status": "A",
#         },
#         {
#             "item": "journal",
#             "qty": 25,
#             "size": {"h": 14, "w": 21, "uom": "cm"},
#             "status": "A",
#         },
#         {
#             "item": "mat",
#             "qty": 85,
#             "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
#             "status": "A",
#         },
#         {
#             "item": "mousepad",
#             "qty": 25,
#             "size": {"h": 19, "w": 22.85, "uom": "cm"},
#             "status": "P",
#         },
#         {
#             "item": "notebook",
#             "qty": 50,
#             "size": {"h": 8.5, "w": 11, "uom": "in"},
#             "status": "P",
#         },
#         {
#             "item": "paper",
#             "qty": 100,
#             "size": {"h": 8.5, "w": 11, "uom": "in"},
#             "status": "D",
#         },
#         {
#             "item": "planner",
#             "qty": 75,
#             "size": {"h": 22.85, "w": 30, "uom": "cm"},
#             "status": "D",
#         },
#         {
#             "item": "postcard",
#             "qty": 45,
#             "size": {"h": 10, "w": 15.25, "uom": "cm"},
#             "status": "A",
#         },
#         {
#             "item": "sketchbook",
#             "qty": 80,
#             "size": {"h": 14, "w": 21, "uom": "cm"},
#             "status": "A",
#         },
#         {
#             "item": "sketch pad",
#             "qty": 95,
#             "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
#             "status": "A",
#         },
#     ]
# collection.insert_many(data)
# record = collection.find()
# record = collection.find({'status':'A'})
# record = collection.find({'status':{'$in':['A','P']}})
# record = collection.find({'status':{'$gt':'C'}})
# record = collection.find({'qty':{'$gte':75}})
# record = collection.find({'item':'sketch pad','qty': {'$gte':75}})
record = collection.find({'$or': [{'item': 'sketch pad'}, {'qty': {'$gte': 75}}]})


# collection.update_one({'item': 'canvas'},{'$set':{'item': 'pooja'}})
# record = collection.find({'item': 'pooja'})
# collection.delete_one({'item': 'pooja'})
# record = collection.find({'item': 'pooja'})
for i in record:
    print(i)
