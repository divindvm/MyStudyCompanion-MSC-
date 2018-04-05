import RPi.GPIO as GPIO
import time
#GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
pin_to_circuit= 31

GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
def rc_time(pin_to_circuit):
	count=0

	GPIO.setup(pin_to_circuit,GPIO.OUT)
	GPIO.output(pin_to_circuit,GPIO.LOW)
	time.sleep(0.1)
	
	GPIO.setup(pin_to_circuit,GPIO.IN)
	
	while(GPIO.input(pin_to_circuit)==GPIO.LOW):
		count+=1
	return count

try:
	while True:
		print rc_time(pin_to_circuit)
		value= rc_time(pin_to_circuit)
		if(value>16000):
                        GPIO.output(32, GPIO.HIGH)
                        GPIO.output(36, GPIO.HIGH)
                if(value<7800):
                        GPIO.output(32, GPIO.LOW)
                        GPIO.output(36, GPIO.LOW)
			
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
