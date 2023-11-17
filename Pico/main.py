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


# motor0.full_turn(10, 1)

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



# import socket

# s = socket.socket()
# addr = socket.getaddrinfo('0.0.0.0', 3000)[0][-1]
# s.bind(addr)
# s.listen(1)
# print("starting true schleife")
# while True:
#     cl, addr = s.accept()
#     request = cl.recv(1024)
#     request = str(request)
#     value = request.split("value=")[1]
#     print("Received slider value:", value)
#     cl.close()



try:
    import usocket as socket
except:
    import socket

import ujson

def web_page():
  return """<html><head></head><body><h1>MicroPython Server</h1></body></html>"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8000))
s.listen(5)



while True:
  conn, addr = s.accept()
  request = conn.recv(1024)
  request = str(request)
  print('Inhalt = %s' % request)
  if (request.find('POST') == 6):
    json_str = request[request.find('{'):request.find('}')+1]
    json_obj = ujson.loads(json_str)
    print(json_obj) # Hier können Sie mit dem empfangenen JSON-Objekt arbeiten
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()