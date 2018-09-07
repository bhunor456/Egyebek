import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
#GPIO.setup(11,GPIO.OUT)

p = GPIO.PWM(7,50)
#p = GPIO.PWM(11,50)
p.start(7.5)
#p.start(11.5)
print("Nóta indul!")

try:
    while True: 
        p.ChangeDutyCycle(7.5) # semleges (neutral)
        #p.ChangeDutyCycle(11.5)
        print("semleges (neutral)")
        time.sleep(1)
        p.ChangeDutyCycle(12.5) # itt fordul el 180 fokot
        #p.ChangeDutyCycle(12.5)
        print("180 fok")
        time.sleep(1)
        p.ChangeDutyCycle(2.5) # 0 fok lesz
       # p.ChangeDutyCycle(2.5)
        print("0 fok")
        time.sleep(1)

except KeyboardInterrupt:
    print("A program leállt")
    p.stop()

    GPIO.cleanup()







