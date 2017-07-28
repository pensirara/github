from flask import Flask
from flask import request
from flask import render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
def shutdown_server():
    func=request.environ.get('werkzeug.server.shutdown')
    if func is None:
      raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down..'

@app.route("/LED/ON")
def ledon():
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, GPIO.HIGH)
    return "led test"

@app.route("/")
def index():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
