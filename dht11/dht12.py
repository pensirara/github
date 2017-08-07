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
@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down..'
@app.route('/a2' ,methods=['POST'])
def root1():
    hour=request.form['hour']
    mn=request.form['mn']
    db=MySQLdb.connect("localhost","root","1234","new1")
    cur=db.cursor()
    cur.execute("select * from dht22 where hour=%s and min=%s"%(hour,mn))
    row=cur.fetchall()
    templatedata={'data':row}
    return render_template('a2.html',**templatedata)

    cur.close()
    db.close()

@app.route('/')
def root():
    return render_template('a1.html')


if __name__=="__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
    

