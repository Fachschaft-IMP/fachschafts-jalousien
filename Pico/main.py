# import machine
# import utime

# dir_pin = machine.Pin(1, machine.Pin.OUT)
# step_pin = machine.Pin(0, machine.Pin.OUT)

# def step(steps, delay):
#     for i in range(steps):
#         step_pin.value(1)
#         utime.sleep_us(delay)
#         step_pin.value(0)
#         utime.sleep_us(delay)

# step(200, 5000)

# delay = 508 # initial delay
# counter = 0

# while True:
#     #if counter % 5 == 0:
#     #    delay += 50 # increase delay by 100 microseconds every 20 seconds
#     step(1, 200, delay) # clockwise
#     # step(0, 200, delay) # counterclockwise
# #     counter += 1

# from machine import Pin
# import utime

# # # Define pin connections & motor's steps per revolution
# dirPin = Pin(1, Pin.OUT)
# stepPin = Pin(0, Pin.OUT)
# led = Pin("LED")
# led.toggle()
# stepsPerRevolution = 200

# # Set motor direction clockwise
# dirPin.value(1)

# # Spin motor slowly
# for x in range(stepsPerRevolution):
#     stepPin.value(1)
#     utime.sleep_us(2000)
#     stepPin.value(0)
#     utime.sleep_us(2000)

# utime.sleep(1)  # Wait a second

# # Set motor direction counterclockwise
# dirPin.value(0)

# # Spin motor quickly
# for x in range(stepsPerRevolution):
#     stepPin.value(1)
#     utime.sleep_us(1000)
#     stepPin.value(0)
#     utime.sleep_us(1000)
# utime.sleep(1)  # Wait a second



# from nemastepper import Stepper
# import time
# stepper = Stepper(1, 0, 13)
# stepper.set_speed(1)

# stepper.do_step()

# for i in range(100):
#     stepper.do_step()
#     time.sleep_ms(10)

# # # from AccelStepper import AccelStepper

# # # stepper = AccelStepper()
# # # stepper.

import time
from machine import Pin

# Definieren Sie die Pins für Schritt und Richtung
step_pin = Pin(0, Pin.OUT)  # Ändern Sie 12 in Ihre Schritt-Pin-Nummer
dir_pin = Pin(1, Pin.OUT)  # Ändern Sie 13 in Ihre Richtung-Pin-Nummer

# Setzen Sie die Richtung
dir_pin.value(0)  # 1 für Uhrzeigersinn, 0 für Gegenuhrzeigersinn

# Definieren Sie die Anzahl der Schritte und die Verzögerung zwischen den Schritten
steps = 2000
delay = 0.001

# Drehen Sie den Motor
for _ in range(steps):
    step_pin.value(1)
    time.sleep(delay)
    step_pin.value(0)
    time.sleep(delay)
