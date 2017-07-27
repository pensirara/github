import MySQLdb

db = MySQLdb.connect("localhost","root","1234","SCOTT")
cur=db.cursor()
cur.execute("select * from EMP where job='manager'")
rs=cur.fetchall()


for i in rs:
    print(i)

cur.close()
db.close()
