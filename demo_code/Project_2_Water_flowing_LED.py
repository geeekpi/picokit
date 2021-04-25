
from machine import Pin
from time import sleep_us

 
LED1 = Pin(0, Pin.OUT)
LED2 = Pin(1, Pin.OUT)
LED3 = Pin(2, Pin.OUT)
LED4 = Pin(3, Pin.OUT)

while True:
    LED1.toggle()
    sleep_us(0.2)
    LED2.toggle()
    sleep_us(0.2)
    LED3.toggle()
    sleep_us(0.2)
    LED4.toggle()
    sleep_us(0.2)

