import RPi.GPIO as GPIO
import keyboard
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

servo= GPIO.PWM(21,50)
print('wait 1 sec please')
servo.start(0)

duty= 0
num= 1
try:
   for i in range(3):
        if keyboard.is_pressed('space'):
            break
        servo.ChangeDutyCycle(10)
        time.sleep(1)
        servo.ChangeDutyCycle(6)
        print(num)
        time.sleep(1)
        num+= 1
        servo.ChangeDutyCycle(2)
        time.sleep(1)
        
except KeyboardInterrupt:
    pass

servo.stop()
GPIO.cleanup()
print('Done')
