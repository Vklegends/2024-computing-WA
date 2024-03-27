#!/usr/bin/env python
# coding: utf-8

# In[44]:


#Mongodb
import pymongo

#connect to the database
client = pymongo.MongoClient("mongodb://localhost:27017/")
#creating a database called mydatbase
mydb = client["mydatabase1"]
#creating a collection
mycollection1 = mydb["mycollection1"]

#inserting document into collection
data = [
    {
        "name": "John",
        "age": 30,
        "city": "New York",
        "occupation": "Engineer"
    },
    {
        "name": "Alice",
        "age": 25,
        "city": "Los Angeles",
        "email": "alice@example.com",
        "interests": ["reading", "traveling"]
    },
    {
        "name": "Bob",
        "age": 35,
        "city": "Chicago",
        "is_student": "false",
        "grades": {"math": 85, "science": 78, "history": 92}
    }
]

#insert multiple documents into collection
# x = mycollection1.insert_many(data)

# #read one
# x = mycollection1.find_one()
# print(x)

# #update
# print("updating document")
# mycollection.update_one({"name": "John"},{"$set": {"age": 32}})
# print(mycollection1.find_one({"name": "John"}))

# #query
# myquery = {"city" : "Chicago"}
# mydocument = mycollection1.find(myquery)

# 2
# #sort
# mydocument = mycollection.find().sort("city")
# for x in mydocument:
#     print(x)

#read all
for x in mycollection1.find():
    print(x)
    
#insert extra john
# mycollection1.delete_one({'name': 'John', 'age': 30, 'city': 'New York', 'occupation': 'Engineer'})
client.close()


# In[ ]:





# In[ ]:




