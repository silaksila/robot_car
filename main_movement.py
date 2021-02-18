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

running = False
try:
    # main script
    while True:
        too_close = distance_sensor.distance_is_lower(5.0)

        char = screen.getch()
        if char == ord('q'):  # quit
            break
        if char == ord('w'):  # forward
            # stop for a small amount of time
            if running:
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
                running = True

        elif char == ord('s'):  # bacward
            # stop for a small ammount of time
            if running:
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
                GPIO.output(14, False)
                GPIO.output(15, True)
                GPIO.output(23, False)
                GPIO.output(24, True)
                running = True

        elif char == ord('b') or too_close:  # stop
            GPIO.output(14, False)
            GPIO.output(15, False)
            GPIO.output(23, False)
            GPIO.output(24, False)
            running = False

        if char == ord('a'):  # turn left
            volant.ChangeDutyCycle(10)
            time.sleep(1)
            volant.ChangeDutyCycle(6)
        elif char == ord('d'):  # turn righ
            volant.ChangeDutyCycle(2)
            time.sleep(1)
            volant.ChangeDutyCycle(6)
        else:
            volant.ChangeDutyCycle(6)
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