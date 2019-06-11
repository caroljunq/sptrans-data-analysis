#  Testing Python + Mongo
# Links
# https://www.datacamp.com/community/tutorials/introduction-mongodb-python
# Another ODM https://github.com/namlook/mongokit
from pymongo import MongoClient
from mongoengine import *

# Connection
client = MongoClient('mongodb://localhost:27017/')

# Creating db
db = client['datacampdb']

article = {"author": "Derrick Mwiti",
            "about": "Introduction to MongoDB and Python",
            "tags":
                ["mongodb", "python", "pymongo"]}

# Creating a collection
articles = db.articles

# Insert a documento into a collection
result = articles.insert_one(article)

print("First article key is: {}".format(result.inserted_id))

# Printing collections
print(db.list_collection_names())

# Inserting multiples documents
article1 = {"author": "Emmanuel Kens",
            "about": "Knn and Python",
            "tags":
                ["Knn","pymongo"]}
article2 = {"author": "Daniel Kimeli",
            "about": "Web Development and Python",
            "tags":
                ["web", "design", "HTML"]}
new_articles = articles.insert_many([article1, article2])
print("The new article IDs are {}".format(new_articles.inserted_ids))

# Retrieving documents
for article in articles.find():
  print(article)
# print(articles.find_one(query here))

## Retrieving n documents using .limit()
limited_result = articles.find().limit(1)
for x in limited_result:
    print(x)

# Eliminating fields --> you can eliminate 1 field specifying the field with 0
for article in articles.find({},{ "_id": 0, "author": 1, "about": 1}):
  print(article)

# Sorting results
# articles.find().sort("field", -1), -1 reverse, 1 ascending
doc = articles.find().sort("author", -1)


for x in doc:
  print(x)

# Updating document
query = { "author": "Derrick Mwiti" }
new_author = { "$set": { "author": "John David" } }
articles.update_one(query, new_author)

for article in articles.find():
  print(article)

# Deleting documents
db.articles.delete_one({"author": "Daniel Kimeli"})
db.articles.delete_many({"author": "Daniel Kimeli"})
# deletes all documents
delete_articles = articles.delete_many({})

for article in articles.find():
  print(article)

# Dropping a collection
articles.drop()
print(db.list_collection_names())

# Object document mapper (ODM)
connect('datacampdb', host='localhost', port=27017)

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=30)
    last_name = StringField(max_length=30)

class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)

user = User(email="connect@derrickmwiti.com", first_name="Derrick", last_name="Mwiti")
user.save()
print(user.id, user.email, user.first_name, user.last_name)

