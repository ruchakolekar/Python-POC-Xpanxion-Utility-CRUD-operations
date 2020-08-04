import cx_Oracle        #Importing library

dsn_tns = cx_Oracle.makedsn('DESKTOP-3J4SO2N', '1521', service_name='XE')
#create connection
conn = cx_Oracle.connect(user=r'SYSTEM', password='agriculture', dsn=dsn_tns)

#print version to check successful connection
print(conn.version)

#create cursor for performing CRUD operations
mycursor = conn.cursor()


#create table in database
mycursor.execute("create table books(name varchar(50), price int)")
conn.commit()


#Insert records in table
mycursor.execute("insert into books(name,price) values('Stories',100)")
mycursor.execute("insert into books(name,price) values('Poems',200)")
mycursor.execute("insert into books(name,price) values('Novels',300)")
conn.commit()


#Read all records from table
mycursor.execute("select * from books")
for row in mycursor:
    print(row)


#Read one record from table
mycursor.execute("select * from books")
row = mycursor.fetchone()
for r in row:
    print(r)


#Read records from table using some filter
mycursor.execute("select name from books where price>100")
for row in mycursor:
    print(row)


#Update records in table
mycursor.execute("update books set price=500 where name='Poems'")
conn.commit()

#Delete record from table
mycursor.execute("delete from books where price=300")
conn.commit()