import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(17, GPIO.IN) #echo pin

