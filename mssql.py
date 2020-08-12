#Importing pyodbc library for connecting to MS-SQL database
import pyodbc

#Establish connection
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-3J4SO2N;"
    "Database=;"
    "Trusted_Connection=yes;"
)
print(conn)

#Create Cursor
cursor = conn.cursor()
conn.autocommit = True


# #Create table in database
# cursor.execute('create table buildings(name varchar(10), flats int)')
# conn.commit()


#Insert records in table
def insert(name,flats):
    cursor.execute("insert into buildings(name,flats) values(?,?)",(name,flats))
    conn.commit()


#Read records from table
             
def read():
    cursor.execute('select * from buildings')
    for row in cursor:
        print(row)



# #Updating records in table
def update(flats,name):
    cursor.execute('update buildings set flats=? where name=?;',(flats,name))
    conn.commit()


#Deleting records from table
def delete(flats):
    cursor.execute('delete from buildings where flats=?;',(flats))
    conn.commit()