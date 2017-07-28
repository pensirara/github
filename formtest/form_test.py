from flask import Flask
from flask render_template
from flask import request

app=Flask(__name)
def shutdown_server():
  func=request.envion.get('werkzeug.server.shutdown')
  if func is None:
    raise RuntimeError('Not running with the Werkzeug Server')
  func()

@app.route('/shutdown')
def shutdown():
  shutdown_server()
  return 'Server shutting down..'

@app.route('/mainpage' method=['POST'])
def mainpage(): #콜백 호출안해도 실행됨
    name=request.form['name']
    nameData={'name':name}
    return render_template('test5.heml',**nameData)
