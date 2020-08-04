import mysql.connector
#mydb = mysql.connector.connect(host="localhost", user="root", passwd="agriculture")
mydb = mysql.connector.connect(host="localhost", user="root", passwd="agriculture", database="Library")
mycursor = mydb.cursor()

#Cret=ating database
mycursor.execute("create database Library")

#Viewing Databases
mycursor.execute("show databases")
for db in mycursor:
    print(db)


#Creating table in database
mycursor.execute("create table books(name varchar(50), price int)")

#Viewing tables in database
mycursor.execute("show tables")
for tb in mycursor:
    print(tb)



#Inserting records in table
sqlform = "insert into books(name,price) values(%s,%s)"
booklist = [("Stories", 100),("Poems", 200),("Novels", 300)]
mycursor.executemany(sqlform,booklist)
mydb.commit()


#Reading one record from table
mycursor.execute("select name from books")
myresult=mycursor.fetchone()
for row in myresult:
    print(row)

#Reading multiple records from table
mycursor.execute("select * from books")
myresult=mycursor.fetchall()
for row in myresult:
    print(row)


#Updating record in table
sql = "update books set price=500 where name='Novels'"
mycursor.execute(sql)
mydb.commit()


#Deleting record from table
sql = "delete from books where price=200"
mycursor.execute(sql)
mydb.commit()