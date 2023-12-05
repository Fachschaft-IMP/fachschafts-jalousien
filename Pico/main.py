import sys
import time
from machine import Pin
from machine import WDT
import urequests

# self written packages
from MotorA4988 import MotorA4988
from Wifi import Wifi
from Wifi import request

# declaring constants
FULL_TURN =  200
MIN_TURN  =  0  * FULL_TURN
MAX_TURN  =  10 * FULL_TURN
URL       = 'http://192.168.1.241:8000/'

# connecting to wifi
wifi = Wifi("Fachschaft IMP", "8clFBb:oR;Q/#scBBj")
wifi.connect()

led = Pin("LED")
led.toggle()


print('Pin.Out is ',Pin.OUT)

motor0 = MotorA4988(Pin( 0, Pin.OUT), Pin( 1, Pin.OUT), Pin( 2, Pin.OUT), MIN_TURN, MAX_TURN)
# motor1 = MotorA4988(Pin( 3, Pin.OUT), Pin( 4, Pin.OUT), Pin( 5, Pin.OUT), MIN_TURN, MAX_TURN)
# motor2 = MotorA4988(Pin( 6, Pin.OUT), Pin( 7, Pin.OUT), Pin( 8, Pin.OUT), MIN_TURN, MAX_TURN)
# motor3 = MotorA4988(Pin( 9, Pin.OUT), Pin(10, Pin.OUT), Pin(11, Pin.OUT), MIN_TURN, MAX_TURN)
# motor4 = MotorA4988(Pin(12, Pin.OUT), Pin(11, Pin.OUT), Pin(14, Pin.OUT), MIN_TURN, MAX_TURN)

motors = [motor0]
# motors = [motor0, motor1, motor2, motor3, motor4]

slider = ['jalou-slider1', 'jalou-slider2', 'jalou-slider3', 'jalou-slider4', 'jalou-slider5', 'master-slider']

import json

request = request("http://192.168.1.253:5000/get-volume")

print("start while true")
print(request.get())
while True:

    data = request.get()

    if data is not None:
        print(data)
        print(data['jalou-slider1'])
        print(data[slider[0]])
        # try:
        index = 0
        value = int(data[slider[index]])
        # für einzelne Motoren hier
        motors[index].bring_to_relative_position(value/100, 50)
        print("brang to positn", value)
        # except:
        #     # Master slider shit hier
        #     print("Master-slider")
        #     value = data[slider[-1]]
        #     MotorA4988.bring_to_relative_positions(motors, value/100, 50)
        #     # for motor in motors:
        #     #     motor.bring_to_relative_position(value/100, 50)

    time.sleep(2)

