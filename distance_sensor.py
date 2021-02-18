import RPi.GPIO as GPIO
import time


def setup():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(17, GPIO.IN)  # echo pin


def measure_distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance


def distance_is_lower(leng):
    if measure_distance() < leng:
        print("Close!!!")
        return True
    return False
