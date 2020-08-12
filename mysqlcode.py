import mysql.connector
#mydb = mysql.connector.connect(host="localhost", user="root", passwd="agriculture")
mydb = mysql.connector.connect(host="localhost", user="root", passwd="agriculture", database="uni")
mycursor = mydb.cursor()

# #Creating database
# mycursor.execute("create database Library")

# #Creating table in database
# mycursor.execute("create table books(name varchar(50), price int)")

#Viewing Databases
def showdb():
    mycursor.execute("show databases")
    for db in mycursor:
        print(db)



#Viewing tables in database
def showtb():
    mycursor.execute("show tables")
    for tb in mycursor:
        print(tb)


#Inserting records in table
def insert(booklist):
    sqlform = "insert into books(name,price) values(%s,%s)"
    mycursor.executemany(sqlform,booklist)
    mydb.commit()


#Reading one record from table
def readone():
    mycursor.execute("select * from books")
    myresult=mycursor.fetchone()
    for row in myresult:
        print(row)

#Reading multiple records from table
def readall():
    mycursor.execute("select * from books")
    myresult2=mycursor.fetchall()
    for row2 in myresult2:
        print(row2)


#Updating record in table
def update(price,name):
    mycursor.execute("update books set price=%s where name=%s",(price,name))
    mydb.commit()


#Deleting record from table
def delete(price):
    sql = """delete from books where price = %s"""
    mycursor.execute(sql, (price,))
    mydb.commit()