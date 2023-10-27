# import machine
# import utime

# step_pin = machine.Pin(14, machine.Pin.OUT)
# dir_pin = machine.Pin(15, machine.Pin.OUT)

# def step(direction, steps, delay):
#     dir_pin.value(direction)
#     for i in range(steps):
#         step_pin.value(1)
#         utime.sleep_us(delay)
#         step_pin.value(0)
#         utime.sleep_us(delay)

# delay = 508 # initial delay
# counter = 0

# while True:
#     #if counter % 5 == 0:
#     #    delay += 50 # increase delay by 100 microseconds every 20 seconds
#     step(1, 200, delay) # clockwise
#     # step(0, 200, delay) # counterclockwise
#     counter += 1

from machine import Pin
import utime

# # Define pin connections & motor's steps per revolution
dirPin = Pin(15, Pin.OUT)
stepPin = Pin(14, Pin.OUT)
led = Pin("led")
led.toggle()
stepsPerRevolution = 200

# Set motor direction clockwise
dirPin.value(1)

# Spin motor slowly
for x in range(stepsPerRevolution):
    stepPin.value(1)
    utime.sleep_us(2000)
    stepPin.value(0)
    utime.sleep_us(2000)

utime.sleep(1)  # Wait a second

# Set motor direction counterclockwise
dirPin.value(0)

# Spin motor quickly
for x in range(stepsPerRevolution):
    stepPin.value(1)
    utime.sleep_us(1000)
    stepPin.value(0)
    utime.sleep_us(1000)

utime.sleep(1)  # Wait a second



# from Pico.nemastepper import Stepper

# stepper = Stepper(15, 14, 13)
# stepper.set_speed(2)

# # stepper.do_step()

# for i in range(100):
#     print("step")
#     stepper.do_step()


