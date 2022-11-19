/* 
================================================================
    Title: Logan-assignment-5.2-projections.js
    Author: Carl Logan
    Date: 11/18/2022
    Description: MongoDB queries using insertOne, updateOne and projections
================================================================
*/

// add a new user to the users collection
db.users.insertOne(
    {
        firstName: 'Joe',
        lastName: 'Shmoe',
        employeeId: '1015',
        email: 'jshmoe@me.com',
        dateCreated: new ISODate()
    }
);

// update the email of an existing document
db.users.updateOne(
    { lastName: 'Mozart' },
    { $set:
        { email: 'mozart@me.com' }
    }
);

// query the document that was just updated
db.users.find({lastName: 'Mozart'});

// find all documents and project firstName, lastName and email
db.users.find(
    {},
    {_id: 0, firstName: 1, lastName: 1, email: 1}
).forEach(printjson);