import sqlite3
con=sqlite3.connect("database.db")
print("connection established")
# con.execute("CREATE TABLE STUDENT (NAME varchar(20), ROLLNO int , PLACE varchar(30))")
x=con.execute("SELECT * FROM STUDENT")
for i in x:
    print(i)
con.commit()
con.close()