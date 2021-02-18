import RPi.GPIO as GPIO
import time


def start():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.OUT)


def led_off():
    print('Led off')
    GPIO.output(16, False)


def led_on():
    print('LED on')
    GPIO.output(16, True)


def ende():
    GPIO.cleanup()
