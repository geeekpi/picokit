from machine import Pin, I2C
from machine_i2c_lcd import I2cLcd
import utime
from time import sleep

trigger = Pin(3, Pin.OUT)

echo = Pin(2, Pin.IN)

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
addr = i2c.scan()[0]
# print(hex(addr[0]))
lcd = I2cLcd(i2c, addr, 2, 16)

def ultrasonic():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   # print("The distance from object is ",distance,"cm")
   return distance


while True:
   distance = ultrasonic()
   utime.sleep(1)
   lcd.putstr("Distance Detect:\n")
   lcd.putstr("Distance is:%.2f" % distance)
   sleep(0.2)
   lcd.clear()
