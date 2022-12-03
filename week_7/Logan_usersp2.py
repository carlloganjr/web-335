"""
================================================================
    Title: Logan_usersp2.py
    Author: Carl Logan
    Date: 11/27/2022
    Description: Python with MongoDB.
================================================================
"""
# import MongoClient
from pymongo import MongoClient
import datetime

# connect to MongoDB web335DB
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.dbdc0d0.mongodb.net/web335DBretryWrites=true&w=majority")

# print connection message to the console
print(client)

# establish the database variable
db = client["web335DB"]

# create a new document in the users collection
db.users.insert_one({
  "firstName": "Johnny",
  "lastName": "Test",
  "employeeId": "1020",
  "email": "jtest@me.com",
  "dateCreated": datetime.datetime.now()
})

# query and print the collection for the updated document
print(db.users.find_one({
  "firstName": "Johnny",
  "lastName": "Test"
}))

# update the email for the new document
db.users.update_one(
  {"firstName": "Johnny", "lastName": "Test"},
  {"$set": {"email": "johnnytest@me.com"}}
)

# query and print the collection for the updated document
print(db.users.find_one({
  "firstName": "Johnny",
  "lastName": "Test"
}))

# delete a specific document
db.users.delete_one({
  "firstName": "Johnny",
  "lastName": "Test"
})

# query the collection for a specific document
print(db.users.find_one({
  "firstName": "Johnny",
  "lastName": "Test"
}))