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

@app.route('/') #http://192.168.1.111:8888
def hello():
	db = MySQLdb.connect("localhost", "root", "1234", "SCOTT")
	cur = db.cursor()
	cur.execute("select empno, ename from EMP")
	row = cur.fetchall()

	templateData = {'data' : row} #row는 2차원 배열
	#{'data':row{'empno' : value , 'ename' : value}}
	return render_template('test2.html', **templateData)
	
	cur.close()
	db.close()

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8888, debug=True)







