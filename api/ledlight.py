import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
print ('LED ON')

GPIO.output(16,True)
time.sleep(1)
print ('LED off')
GPIO.output(16,False)

GPIO.cleanup()
