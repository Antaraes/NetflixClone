from django.test import TestCase
import pymongo
# Create your tests here.
connection = pymongo.MongoClient('localhost',27017)
database = connection['netflixDB']
collection = database['auth_user']
data = {
  "password": "pass",
  "username": "ajm",
  "first_name": "",
  "last_name": "",
  "email": "",
}
try:
    collection.insert_one(data)
    print('success')
except:
    print('err')
