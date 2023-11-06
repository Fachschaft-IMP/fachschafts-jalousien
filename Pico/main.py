import sys
import time
from machine import Pin
from machine import WDT
import json
import urequests

# self written packages
from MotorA4988 import MotorA4988
from Wifi import Wifi

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

# motors = [motor0, motor1, motor2, motor3, motor4]


motor0.full_turn(10, 1)

# #################################################################################################
# import concurrent.futures

# def full_turn_all(motors):
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         # Starten Sie die full_turn-Methode für jeden Motor in einem separaten Thread
#         futures = [executor.submit(motor.full_turn, 1, 1) for motor in motors]
        
#         # Warten Sie, bis alle Threads abgeschlossen sind
#         concurrent.futures.wait(futures)


# full_turn_all(motors)
# #################################################################################################

# slider_value = 0

# # Funktion zum Behandeln der HTTP-Anfrage
# def set_slider_value(request):
#     global slider_value
#     slider_value = int(request.args.get("value"))
#     return "OK"

