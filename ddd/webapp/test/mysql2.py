import MySQLdb

db = MySQLdb.connect("localhost","root","1234","SCOTT")
cur=db.cursor()

sql="insert into EMP(empno,ename,job) values(777,'401ho','student')"
try:
    cur.execute(sql)
    db.commit()
except:
    db.rollback()

sql="select * from EMP"
cur.execute(sql)
rs=cur.fetchall()
for i in rs:
    print(i)

print("===============")

sql="delete from EMP where empno=777"
cur.execute(sql)
db.commit()

sql="select * from EMP"
cur.execute(sql)
rs=cur.fetchall()
for i in rs:
    print(i)


cur.close()
db.close()
