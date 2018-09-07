import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)

for x in range(0,12):
    GPIO.output(7,True)
    time.sleep(0.0625)
    GPIO.output(7,False)
    time.sleep(0.0625)
    GPIO.output(11,True)
    time.sleep(0.0625)
    GPIO.output(11,False)
    time.sleep(0.0625)
    GPIO.output(13,True)
    time.sleep(0.0625)
    GPIO.output(13,False)
    time.sleep(0.25)
    GPIO.output(37,True)
    time.sleep(0.0625)
    GPIO.output(37,False)
    time.sleep(0.0625)
GPIO.cleanup()









