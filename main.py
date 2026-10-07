from machine import Pin, PWM
from time import sleep

# FoCar motor pins configuration
e1 = PWM(Pin(28))  # Left Motor Speed Control
m1 = Pin(27, Pin.OUT)  # Left Motor Direction Control

e2 = PWM(Pin(26))  # Right Motor Speed Control
m2 = Pin(22, Pin.OUT)  # Right Motor Direction Control

# Set PWM frequency
e1.freq(1000)
e2.freq(1000)

# Motor Speed (0 to 65535)
SPEED = 32767  # 50% Speed

# Timing
TIME_0_5M = 1.0
TIME_90_DEG = 0.5
TIME_180_DEG = 1.0


def stop():
    e1.duty_u16(0)
    e2.duty_u16(0)
    m1.value(0)
    m2.value(0)
    sleep(0.2)


def move_forward(duration):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(SPEED)
    e2.duty_u16(SPEED)
    sleep(duration)
    stop()


def move_backward(duration):
    m1.value(0)
    m2.value(0)
    e1.duty_u16(SPEED)
    e2.duty_u16(SPEED)
    sleep(duration)
    stop()


def turn_left(duration):
    m1.value(0)
    m2.value(1)
    e1.duty_u16(SPEED)
    e2.duty_u16(SPEED)
    sleep(duration)
    stop()


def turn_right(duration):
    m1.value(1)
    m2.value(0)
    e1.duty_u16(SPEED)
    e2.duty_u16(SPEED)
    sleep(duration)
    stop()


def turn_180():
    turn_left(TIME_180_DEG)


# Start delay
sleep(2)

# Read movement instructions from file
with open("instructions.txt", "r") as file:
    instructions = file.readlines()

# Execute instructions
for instruction in instructions:
    command = instruction.strip()

    if command == "FORWARD":
        move_forward(TIME_0_5M)

    elif command == "BACKWARD":
        move_backward(TIME_0_5M)

    elif command == "LEFT":
        turn_left(TIME_90_DEG)

    elif command == "RIGHT":
        turn_right(TIME_90_DEG)

    elif command == "TURN180":
        turn_180()

    elif command == "":
        continue
