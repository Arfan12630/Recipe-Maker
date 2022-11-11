from pymongo import MongoClient


db = cluster['recipe']

# create collection
db_collection_dinner = db['dinner']

