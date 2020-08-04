import psycopg2

con = psycopg2.connect(
    host = "DESKTOP-NA6MIUR",
    database = "py",
    user = "postgres",
    password = "9823",
    port = 5432  
)
print("iuihib")

cur = con.cursor()
cur.execute("insert into something (add,sub) values (9, 'div')")
cur.execute("select add,sub from something")

rows = cur.fetchall()

for r in rows:
    print(f"add{r[0]} sub {r[1]}")
    

con.commit()
cur.close()
con.close()