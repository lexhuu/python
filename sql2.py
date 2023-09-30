import sqlite3
con=sqlite3.connect("database.db")
print("connection established")
con.execute("CREATE TABLE HOSPITAL (EmployeeID int primary key, Ename varchar(20), DeptID int, Salary int, Dname varchar(20), Dlocation varchar(30))")
con.execute("INSERT INTO HOSPITAL VALUES (1,'John',2,4000,'IT','New Delhi')")
con.execute("INSERT INTO HOSPITAL VALUES (2,'Anna',1,3500,'HR','Mumbai')")
con.execute("INSERT INTO HOSPITAL VALUES (3,'James',1,2500,'HR','Mumbai')")
con.execute("INSERT INTO HOSPITAL VALUES (4,'David',2,5000,'IT','New Delhi')")
con.execute("INSERT INTO HOSPITAL VALUES (5,'Mark',2,3000,'IT','New Delhi')")
con.execute("INSERT INTO HOSPITAL VALUES (6,'Steve',3,4500,'FINANCE','Mumbai')")
con.execute("INSERT INTO HOSPITAL VALUES (7,'Alice',3,3500,'FINANCE','Mumbai')")

x=con.execute("update HOSPITAL set Dname = 'Software' where EmployeeID = 1006")
x=con.execute("SELECT * FROM HOSPITAL")
for i in x:
    print(i)
con.commit()
con.close()