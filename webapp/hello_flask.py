from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
    return "dsfsdfHello RasberryPi with Flask!!"
if __name__=="__main__":
    app.run(host='0.0.0.0',port=1234,debug=True)
    
