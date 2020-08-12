import cx_Oracle        #Importing library

dsn_tns = cx_Oracle.makedsn('DESKTOP-3J4SO2N', '1521', service_name='XE')
#create connection
conn = cx_Oracle.connect(user=r'SYSTEM', password='agriculture', dsn=dsn_tns)

#print version to check successful connection
print(conn.version)

#create cursor for performing CRUD operations
mycursor = conn.cursor()


# #create table in database
# mycursor.execute("create table books(name varchar(50), price int)")
# conn.commit()


#Insert records in table
def insert(name,price):
    sql = 'insert into books(name,price) values(:name,:price)'
    mycursor.execute(sql, name=name, price=price)
    conn.commit()


#Read all records from table
def readall():
    mycursor.execute("select * from books")
    for row in mycursor:
        print(row)


#Read one record from table
def readone():
    mycursor.execute("select * from books")
    row = mycursor.fetchone()
    for r in row:
        print(r)


#Read records from table using some filter
def readf(price):
    sql = 'select name from books where price= :price'
    mycursor.execute(sql, price=price)
    for row in mycursor:
        print(row)


#Update records in table
def update(price,name):
    sql = "update books set price= :price where name= :name"
    mycursor.execute(sql, price=price, name=name)
    conn.commit()

#Delete record from table
def delete(price):
    sql = "delete from books where price= :price"
    mycursor.execute(sql, price=price)
    conn.commit()