import sys
import time
from machine import Pin
from machine import WDT
import json
import urequests as requests

from MotorA4988 import MotorA4988
from Wifi import Wifi

FULL_TURN = 200
MIN_TURN = 0
MAX_TURN = 10 * FULL_TURN
URL = 'http://192.168.1.241:8000/'


wifi = Wifi("Fachschaft IMP", "8clFBb:oR;Q/#scBBj")
wifi.connect()

led = Pin("LED")
led.toggle()


motor1 = MotorA4988(Pin(0, Pin.OUT), Pin(1, Pin.OUT), Pin(2, Pin.OUT), MIN_TURN, MAX_TURN)
print('Pin.Out is ',Pin.OUT)

motor1.full_turn(1, 1)