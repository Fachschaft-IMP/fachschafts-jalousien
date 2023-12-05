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

import json

request = request("http://192.168.1.253:5000/set-volume")

print("start while true")
print(request.get())
while True:

    jsonString = request.get()
    data = {}
    try:
        data = json.loads(jsonString)
    except:
        data = jsonString
    print(data)
    if data is not None:

        if 'id' in data:
            print(jsonString)
            data = jsonString
            idString = data['id']
            value = data['volume']
            try:
                # für einzelne Motoren hier
                id = int(idString[-1])
                motors[id-1].bring_to_relative_position(value/100, 50)
            except:
                # Master slider shit hier
                print("Master-slider")
                MotorA4988.bring_to_relative_positions(motors, value/100, 50)
                # for motor in motors:
                #     motor.bring_to_relative_position(value/100, 50)

            time.sleep(1)

