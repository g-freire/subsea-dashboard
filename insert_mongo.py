
import pymongo
from random import random
from time import sleep

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["streaming"]
collection = db["pump_001"]


# # query last record from db
# cursor = collection.find().limit(1).sort("_id", -1)

# print(cursor[doc])
# try:
#     for doc in cursor:
#         print(doc)
# finally:
#     client.close()


while 1:
    random_value = round(random()*100, 3)
    mydict = { "name": "pressure", "value": random_value }
    x = collection.insert_one(mydict)     
    print('Inserted value ', random_value)
    sleep(2)