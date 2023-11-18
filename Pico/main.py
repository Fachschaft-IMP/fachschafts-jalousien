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

# motors = [motor0, motor1, motor2, motor3, motor4]


# motor0.full_turn(10, 1)

# #################################################################################################
# import concurrent.futures

# def full_turn_all(motors, turns):
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         # Starten Sie die full_turn-Methode für jeden Motor in einem separaten Thread
#         futures = [executor.submit(motor.full_turn, turns, 1) for motor in motors]
        
#         # Warten Sie, bis alle Threads abgeschlossen sind
#         concurrent.futures.wait(futures)


# full_turn_all(motors)
# #################################################################################################


# import urequests
# import time

# url = "http://localhost:3000/get-volume"
# data_before = None

# while True:
#     try:
#         response = urequests.get(url)

#         data_after = response.json()
#         # Vergleiche die beiden Daten
#         if data_before != data_after:
#             print('Die Daten haben sich geändert:')
#             print('Nachher:', data_after)
#             data_before = data_after
#             time.sleep(2)
#         time.sleep(1)
#     except:
#         print("connection lost")
#         time.sleep(104)

request = request("http://localhost:3000/get-volume")

while True:
    data = request.get()

