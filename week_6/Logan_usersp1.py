"""
================================================================
    Title: Logan_usersp1.py
    Author: Carl Logan
    Date: 11/20/2022
    Description: Python MongoDB connection and use.
================================================================
"""
# import MongoClient
from pymongo import MongoClient

# connect to MongoDB web335DB
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.dbdc0d0.mongodb.net/web335DBretryWrites=true&w=majority")

# print connection message to the console
print(client)

# establish the database variable
db = client["web335DB"]

# find and display all documents in the collection
for user in db.users.find():
   print(user)

# find a document matching the criteria
print(db.users.find_one({'employeeId': "1011"}))

# find a document matching the criteria
print(db.users.find_one({'lastName': "Mozart"}))