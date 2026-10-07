from machine import Pin, PWM
from time import sleep

# FoCar motor pins configuration
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

e1.freq(1000)
e2.freq(1000)

SPEED = 32767
