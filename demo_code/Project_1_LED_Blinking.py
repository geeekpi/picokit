import time
from machine import Pin

 
LED = Pin(0, Pin.OUT)

while True:
    LED.value(0)
    time.sleep(0.5)
    LED.value(1)
    time.sleep(0.5)

