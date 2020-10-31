import os
import time
from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost', 27017)
db = client.SistemaPi

cursor = db.temperatura.find({})
for document in cursor: 
    pprint(document)
       