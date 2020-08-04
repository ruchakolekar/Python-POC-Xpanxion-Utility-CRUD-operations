from pymongo import MongoClient  #Import pymongo library
import pprint                    #for printing in presentable manner

client = MongoClient()           #create Mongodb client
db = client.udemy                #create database or use existing one
courses = db.courses             #create a collection



#Inserting a single document
course1 = {
    'name': 'Mongodb',
    'author': 'xyz',
    'duration': 25
}

result = courses.insert_one(course1)
if result.acknowledged:
  print('Course added and course id is ' + str(result.inserted_id))



#Inserting Multiple Documents
arr_courses = [
    {
    'name': 'NodeJS',
    'author': 'abc',
    'duration': 30
    },
    {
    'name': 'ReactJS',
    'author': 'pqr',
    'duration': 35
    }
]
result2 = courses.insert_many(arr_courses)
for object_id in result2.inserted_ids:
    print('Course added and course id is ' + str(object_id))




#Retrieving single Document
course = courses.find_one()
print(course)

#Retrieving Multiple Documents
course = courses.find()
for cr in course:
 pprint.pprint(cr)

#Retrieving documents based on some condition
course = courses.find({
    'name': 'NodeJS'
})
for cr in course:
 pprint.pprint(cr)

course2 = courses.find({
    'duration': {
        '$gt': 25
    }
})
for cr2 in course2:
 pprint.pprint(cr2)

#Sorting and limiting documents
course = courses.find().sort([('author',1),('duartion',1)]).limit(2)
for cr in course:
 pprint.pprint(cr)




#Updating documents
courses.update({
    'name': 'Mongodb'
},
{
    '$set': {
        'name': 'Mongodb Guide'
    }
},
multi=True
)



#Deleting single Document
courses.delete_one({
    'name': 'Mongodb Guide'
})

#Deleting multiple Documents
courses.delete_many({
    'name': 'Mongodb Guide'
})


#Printing number of documents in a collection
print(courses.find().count())