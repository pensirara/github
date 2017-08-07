import Adafruit_DHT
import time
import datetime
import MySQLdb
import RPi.GPIO as GPIO

sensor = Adafruit_DHT.DHT11
pin = 24 #GPIO
db=MySQLdb.connect("localhost","root","1234","new1")


while True:
    wtime=datetime.datetime.now()
    print(wtime)
    t_year=wtime.strftime('%Y')
    t_month=wtime.strftime('%m')
    t_day=wtime.strftime('%d')
    t_hour=wtime.strftime('%H')
    t_min=wtime.strftime('%M')
    t_humidity, t_temperature = Adafruit_DHT.read_retry(sensor, pin)
    cur=db.cursor()
    cur.execute("insert into dht22 values(%s, %s, %s, %s, %s, %s, %s)" %(t_year, t_month, t_day, t_hour, t_min, t_humidity, t_temperature))
    db.commit()
    time.sleep(1)



