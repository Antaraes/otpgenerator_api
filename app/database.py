from pymongo import mongo_client
import pymongo
from app.config import settings
client = mongo_client.MongoClient(settings.DATABASE_URL)
print("Connect to mongodb...")

db = client[settings.MONGO_INITDB_DATABASE]
User = db.users
User.create_index([("email",pymongo.ASCENDING)],unique=True)