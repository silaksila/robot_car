
import RPi.GPIO as GPIO
import keyboard
import time
import curses
import distance_sensor

# imput setup
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
screen.nodelay()
######
distance_sensor.setup()
# GPIO numbering
GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)  # Forward
GPIO.setup(15, GPIO.OUT)  # back
GPIO.setup(23, GPIO.OUT)  # Forward
GPIO.setup(24, GPIO.OUT)  # back

GPIO.setup(21, GPIO.OUT)

# servo
volant = GPIO.PWM(21, 50)
volant.start(0)
volant.ChangeDutyCycle(6)
time.sleep(1)

########################################################################################


def forward():
    global moving
    if moving:
        GPIO.output(14, False)
        GPIO.output(15, False)
        GPIO.output(23, False)
        GPIO.output(24, False)

        time.sleep(0.2)

        GPIO.output(14, False)
        GPIO.output(15, True)
        GPIO.output(23, False)
        GPIO.output(24, True)
    else:
        GPIO.output(14, False)
        GPIO.output(15, True)
        GPIO.output(23, False)
        GPIO.output(24, True)
        moving = True


def backward():
    global moving
    if moving:
        GPIO.output(14, False)
        GPIO.output(15, False)
        GPIO.output(23, False)
        GPIO.output(24, False)
        time.sleep(0.2)
        GPIO.output(14, True)
        GPIO.output(15, False)
        GPIO.output(23, True)
        GPIO.output(24, False)
    else:
        GPIO.output(14, True)
        GPIO.output(15, False)
        GPIO.output(23, True)
        GPIO.output(24, False)
        moving = True


def stop():
    global moving
    GPIO.output(14, False)
    GPIO.output(15, False)
    GPIO.output(23, False)
    GPIO.output(24, False)
    time.sleep(0.2)
    moving = False

###########################################################################################


moving = False
try:
    # main script
    while True:
        too_close = distance_sensor.distance_is_lower(10.0)

        char = screen.getch()
        if char == ord('q'):  # quit
            break
        if char == ord('w'):  # forward
            forward()

        elif char == ord('s'):  # bacward
            backward()

        if char == ord('b') or too_close:  # stop
            stop()

        if char == ord('a'):  # turn left
            volant.ChangeDutyCycle(10)
            while char == ord('a'):
                char = screen.getch()
                time.sleep(0.1)
            volant.ChangeDutyCycle(6.5)
        elif char == ord('d'):  # turn righ
            volant.ChangeDutyCycle(2)
            while char == ord('d'):
                char = screen.getch()
                time.sleep(0.1)

            volant.ChangeDutyCycle(6.5)
        else:
            volant.ChangeDutyCycle(6.5)
            time.sleep(0.5)
except KeyboardInterrupt:
    pass
# cleanup
GPIO.output(14, False)
GPIO.output(15, False)
GPIO.output(23, False)
GPIO.output(24, False)

volant.ChangeDutyCycle(2)
time.sleep(1)
volant.stop()
curses.nocbreak()
screen.keypad(0)
curses.echo()
curses.endwin()
GPIO.cleanup()
print("DONE")
