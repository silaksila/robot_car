import time
import RPi.GPIO as GPIO
import keyboard
import curses

#numbering GPIO
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

GPIO.setmode(GPIO.BCM)

GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

GPIO.setup(21,GPIO.OUT)

servo= GPIO.PWM(21,50)

GPIO.output(15,False)
GPIO.output(24,False)
GPIO.output(14,False)
GPIO.output(23,False)
#LOOOL
servo.start(6)
try:
    while True:
        char= screen.getch()
        if char== ord('e'):
            break
        elif char== ord('s'):
            GPIO.output(15,True)
            GPIO.output(24,True)
            GPIO.output(14,False)
            GPIO.output(23,False)
        elif char== ord('a'):
            servo.ChangeDutyCycle(10)
            time.sleep(1)
            servo.ChangeDutyCycle(6)
        elif char== ord('w'):
            GPIO.output(15,False)
            GPIO.output(24,False)
            GPIO.output(14,True)
            GPIO.output(23,True)
        elif char== ord('d'):
            servo.ChangeDutyCycle(2)
            time.sleep(1)
            servo.ChangeDutyCycle(6)
        elif char==ord('b'):
            GPIO.output(15,False)
            GPIO.output(24,False)
            GPIO.output(14,False)
            GPIO.output(23,False)

except KeyboardInterrupt :
    pass
servo.ChangeDutyCycle(6)
servo.stop()
curses.nocbreak()
screen.keypad(0)
curses.echo()
curses.endwin()
GPIO.cleanup()
print('DONE')
