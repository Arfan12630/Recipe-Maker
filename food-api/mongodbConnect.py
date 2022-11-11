from pymongo import MongoClient
cluster = MongoClient('mongodb+srv://Arfan12630:yySDLHzQ1vGjgZU8@cluster0.cdrrsj6.mongodb.net/?retryWrites=true&w=majority')

db = cluster['recipe']

# create collection
db_collection_dinner = db['dinner']

