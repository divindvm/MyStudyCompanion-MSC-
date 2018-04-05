import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#GPIO.cleanup()
GPIO.setup(32,GPIO.OUT)

GPIO.output(32,True)

GPIO.cleanup()



