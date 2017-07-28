import MySQLdb
from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)
def shutdown_server():
    func=request.environ.get('werkzeug.server.shutdown')
    if func is None:
      raise RuntimeError('Not running with the Werkzeug Server')
    func()
@app.route('/create')
def create():
    return render_template('create.html')
  
@app.route('/createidpw',methods=["POST"])
def createidpw():
    cid=request.form['cid']
    cpass=request.form['cpass']
    db=MySQLdb.connect("localhost","root","1234","SCOTT")
    cur=db.cursor()
    cur.execute("insert into IDPW(id,pw) values(%s,%s)",(cid,cpass))
    db.commit()
    return render_template('index.html')
  
    cur.close()
    db.close()
@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down..'

@app.route('/chack' , methods=["POST"])
def sucesstest():
    db=MySQLdb.connect("localhost","root","1234","SCOTT")
    cur=db.cursor()
    ids= request.form['id']
    password=request.form['pass']
    cur.execute("select * from IDPW where id=%s",ids)
    row=cur.fetchone()
    
    if ids==str(row[0]) and password==str(row[1]):
      return render_template('sucess.html')
    else:
      return render_template('index.html')
    
    
    cur.close()
    db.close()
@app.route('/')
def root():
    return render_template('index.html')

if __name__=="__main__":
    app.run(host='0.0.0.0' ,port=8888 ,debug=True)
