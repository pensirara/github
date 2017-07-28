# coding: utf-8

import MySQLdb
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

def shutdown_server():
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
                raise RuntimeError('Not running with the Werkzeug Server')
        func()

@app.route('/shutdown') #http://192.168.1.111:8888/shutdown
def shutdown():
        shutdown_server()
        return 'Server shutting down..'

@app.route('/insert')
def hello1():
        db=MySQLdb.connect("localhost", "root", "1234", "SCOTT")
        cur = db.cursor()
        try:
                cur.execute("insert into EMP(empno,ename)value(333,'ddd')")
                db.commit()
                return 'db data input oo'
        except:
                db.rollback()
                return 'db data nono'
        
        cur.close()
        db.close()
@app.route('/delete')
def hello2():
        db=MySQLdb.connect("localhost", "root", "1234", "SCOTT")
        cur = db.cursor()
        try:
                cur.execute("delete from EMP where empno=333")
                db.commit()
                return 'db data delete oo'
        except:
                db.rollback()
                return 'db data delete nono'
        
        cur.close()
        db.close()
@app.route('/create')
def hello3():
        db=MySQLdb.connect("localhost", "root", "1234", "SCOTT")
        cur = db.cursor()
        try:
                cur.execute("create table KKAA(id int ,name char(20))")
                cur.execute("insert into KKAA(id,name)value(1,'ddd')")
                db.commit()
                return 'db data create oo'
        except:
                db.rollback()
                return 'db data create nono'
        
        cur.close()
        db.close()
@app.route('/cre') #http://192.168.1.111:8888
def hello4():
        db = MySQLdb.connect("localhost", "root", "1234", "SCOTT")
        cur = db.cursor()
        cur.execute("select * from KKAA")
        row = cur.fetchall()

        templateData = {'data' : row} #row는 2차원 배열
        return render_template('test.html', **templateData)

        cur.close()
        db.close()

        
@app.route('/') #http://192.168.1.111:8888
def hello():
        db = MySQLdb.connect("localhost", "root", "1234", "SCOTT")
        cur = db.cursor()
        cur.execute("select empno, ename from EMP")
        row = cur.fetchall()

        templateData = {'data' : row} #row는 2차원 배열
        #{'data':row{'empno' : value , 'ename' : value}}
        return render_template('test.html', **templateData)

        cur.close()
        db.close()
@app.route('/select') #http://192.168.1.111:8888
def hello5():
        db = MySQLdb.connect("localhost", "root", "1234", "SCOTT")
        cur = db.cursor()
        cur.execute("select * from EMP")
        row = cur.fetchall()

        templateData = {'data' : row} #row는 2차원 배열
        #{'data':row{'empno' : value , 'ename' : value}}
        return render_template('test.html', **templateData)

        cur.close()
        db.close()
@app.route('/select/<num>') #http://192.168.1.111:8888
def hello6(num):
        db = MySQLdb.connect("localhost", "root", "1234", "SCOTT")
        cur = db.cursor()
        cur.execute("select * from EMP where empno=%s"%num)
        row = cur.fetchall()

        templateData = {'data' : row} #row는 2차원 배열
        #{'data':row{'empno' : value , 'ename' : value}}
        return render_template('test.html', **templateData)

        cur.close()
        db.close()

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8888, debug=True)







