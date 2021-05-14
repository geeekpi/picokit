from machine import Pin
from time import sleep

 
LED1 = Pin(0, Pin.OUT)
LED2 = Pin(1, Pin.OUT)
LED3 = Pin(2, Pin.OUT)
LED4 = Pin(3, Pin.OUT)

interval = 0.2

while True:
    LED1.toggle()
    sleep(interval)
    LED2.toggle()
    sleep(interval)
    LED3.toggle()
    sleep(interval)
    LED4.toggle()
    sleep(interval)

