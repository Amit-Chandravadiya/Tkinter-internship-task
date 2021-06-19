from pymongo import MongoClient

global client,db,collection
client=MongoClient("mongodb+srv://Amit_Intern:test@cluster0.snmz8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client.get_database('user_auth')
collection=db.users