import LED_control as led
import time

led.start()
time.sleep(1)
led.led_on()
time.sleep(5)
led.ende()
print("DONE")
