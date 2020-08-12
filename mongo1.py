from pymongo import MongoClient  #Import pymongo library
import pprint                    #for printing in presentable manner

client = MongoClient()           #create Mongodb client
db = client.udemy                #create database or use existing one
courses = db.courses             #create a collection



#Inserting a single document

def insertone(course1):
    result = courses.insert_one(course1)
    if result.acknowledged:
        print('Course added and course id is ' + str(result.inserted_id))



#Inserting Multiple Documents
def insertmany(arr_courses):
    result2 = courses.insert_many(arr_courses)
    for object_id in result2.inserted_ids:
        print('Course added and course id is ' + str(object_id))




#Retrieving single Document
def readone():
    course = courses.find_one()
    print(course)

#Retrieving Multiple Documents
def readall():
    course = courses.find()
    for cr in course:
        pprint.pprint(cr)

#Retrieving documents based on some condition
def condition(name):
    course = courses.find({
    'name': name
    })
    for cr in course:
        pprint.pprint(cr)

#Sorting and limiting documents
def limiting(num):
    course = courses.find().limit(num)
    for cr in course:
        pprint.pprint(cr)



#Updating documents
def update(name1,name2):
    courses.update({
    'name': name1
    },
    {
    '$set': {
        'name': name2
    }
    },
    multi=True
    )


#Deleting single Document
def deleteone(name):
    courses.delete_one({
    'name': name
    })

#Deleting multiple Documents
def deletemany(name):
    courses.delete_many({
    'name': name
    })


#Printing number of documents in a collection
def getcount():
    print(courses.find().count())