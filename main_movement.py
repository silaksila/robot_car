import RPi.GPIO as GPIO
import keyboard 
import time
import curses

#imput setup
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

#GPIO numbering
GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)#Forward
GPIO.setup(15, GPIO.OUT)# back
GPIO.setup(23, GPIO.OUT)#Forward
GPIO.setup(24, GPIO.OUT)# back

GPIO.setup(21, GPIO.OUT)

#servo
volant= GPIO.PWM(21, 50)
volant.start(0)
volant.ChangeDutyCycle(6)
time.sleep(1)
try:
    #main script
    while True:
        char= screen.getch()
        if char== ord('q'): #quit
            break
        if char== ord('w'):#forward
            #stop for a small amount of time
            GPIO.output(14, False)
            GPIO.output(15, False)
            GPIO.output(23, False)
            GPIO.output(24, False)
            time.sleep(0.5)
            
            GPIO.output(14, False)
            GPIO.output(15, True)
            GPIO.output(23, False)
            GPIO.output(24, True)
        elif char== ord('s'): #bacward
            #stop for a small ammount of time
            GPIO.output(14, False)
            GPIO.output(15, False)
            GPIO.output(23, False)
            GPIO.output(24, False)
            time.sleep(0.5) 
            GPIO.output(14, True)
            GPIO.output(15, False)
            GPIO.output(23, True)
            GPIO.output(24, False)
        elif char== ord('b'): #stop
            GPIO.output(14, False)
            GPIO.output(15, False)
            GPIO.output(23, False)
            GPIO.output(24, False)



        if char == ord('a'): #turn left
            volant.ChangeDutyCycle(10)
            time.sleep(1)
            volant.ChangeDutyCycle(6)
        elif char == ord('d'): #turn righ
            volant.ChangeDutyCycle(2)
            time.sleep(1)
            volant.ChangeDutyCycle(6)
        else:
            volant.ChangeDutyCycle(6)
            time.sleep(0.5)
except KeyboardInterrupt :
    pass
#cleanup
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

