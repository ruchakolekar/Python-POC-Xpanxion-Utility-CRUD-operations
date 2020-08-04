#Importing pyodbc library for connecting to MS-SQL database
import pyodbc

#Establish connection
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-3J4SO2N;"
    "Database=society;"
    "Trusted_Connection=yes;"
)
print(conn)

#Create Cursor
cursor = conn.cursor()
conn.autocommit = True


#Create table in database
cursor.execute('create table buildings(name varchar(10), flats int)')
conn.commit()


#Insert records in table
cursor.execute('insert into buildings(name ,flats) values(?,?);', ("A",50))
cursor.execute('insert into buildings(name ,flats) values(?,?);', ("B",60))
cursor.execute('insert into buildings(name ,flats) values(?,?);', ("C",70))
conn.commit()


#Read records from table
#I created function for read for multiple usage throughout program for checking update and delete results.
def read(conn):               
    cursor.execute('select * from buildings')
    for row in cursor:
        print(row)

read(conn)


#Updating records in table
cursor.execute('update buildings set flats=? where name=?;',(100,"B"))
conn.commit()
read(conn)


#Deleting records from table
cursor.execute('delete from buildings where flats=?;',(100))
conn.commit()
read(conn)