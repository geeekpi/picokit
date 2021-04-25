from machine import Pin, I2C　
from time import sleep, sleep_ms
from machine_i2c_lcd import I2cLcd

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
addr = i2c.scan()[0]
# print(hex(addr[0]))
lcd = I2cLcd(i2c, addr, 2, 16)
pir_sensor = Pin(15, Pin.IN)

while True:
    reading = pir_sensor.value()
    if reading == '1':
        lcd.putstr("Motion Detect:\n")
        lcd.putstr("Move Detected!")
        sleep(1)
        lcd.clear()
    else:
        lcd.putstr("Motion Detect:\n")
        lcd.putstr("No Move Detect!")
        sleep(1)
        lcd.clear()
