/* 
================================================================
    Title: Logan-MongoDB-Shell.js
    Author: Carl Logan
    Date: 11/12/2022
    Description: Mongo Shell queries in action.
================================================================
*/

// access the users collection to select documents and display each one
print("QUERY FOR ALL DOCUMENTS:");
db.users.find().forEach(printjson);

// find a document with a specific email address and display 
print("QUERY FOR A SPECIFIC EMAIL:");
db.users.find({email: "jbach@me.com"}).forEach(printjson);

// find a document with a specific last name and display
print("QUERY FOR A LAST NAME:"); 
db.users.find({lastName: "Mozart"}).forEach(printjson);

// find a document with a specific first name and display
print("QUERY FOR A FIRST NAME:"); 
db.users.find({firstName: "Richard"}).forEach(printjson);

// find a document with a specific employee id and display
print("QUERY FOR AN EMPLOYEE ID:"); 
db.users.find({employeeId: "1010"}).forEach(printjson);

