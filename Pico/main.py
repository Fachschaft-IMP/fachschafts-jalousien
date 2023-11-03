import sys
import time
import ntptime
from machine import Pin
from machine import WDT
import network
import json
import urequests as requests

# # Wi-Fi-Verbindung herstellen
# wifi = network.WLAN(network.STA_IF)
# wifi.active(True)
# wifi.connect("Fachschaft IMP", "8clFBb:oR;Q/#scBBj")  # SSID und Passwort anpassen

# print("connecting to wifi...")
# while not wifi.isconnected():
#     pass
print('connected')

# Watchdog inizialisieren
wtd = WDT()

url = 'http://192.168.1.241:8000/'
# Schalter an Pin GP14 konfigurieren

step_pins  = [Pin(0, Pin.OUT)]
dir_pins   = [Pin(1, Pin.OUT)]
en_pins    = [Pin(2, Pin.OUT)]
turn_count = [0]
# step_pins  = [Pin(0, Pin.OUT), Pin(3, Pin.OUT), Pin(6, Pin.OUT), Pin( 9, Pin.OUT), Pin(12, Pin.OUT)]
# dir_pins   = [Pin(1, Pin.OUT), Pin(4, Pin.OUT), Pin(7, Pin.OUT), Pin(10, Pin.OUT), Pin(13, Pin.OUT)]
# en_pins    = [Pin(2, Pin.OUT), Pin(5, Pin.OUT), Pin(8, Pin.OUT), Pin(11, Pin.OUT), Pin(14, Pin.OUT)]
# turn_count = [0, 0, 0, 0, 0]

led = Pin("LED")

FULL_TURN = 200
MAX_TURN = 10 * FULL_TURN

def turn_off_motors():
    for pin in en_pins:
        pin.high()

def turn_on_motors():
    for pin in en_pins:
        pin.low()

def switch_dir(dir:int):
    for pin in dir_pins:
        pin.value(dir)

# def step(steps, delay):
#     for pin in step_pins:
#         for i in range(steps):
#             pin.value(1)
#             time.sleep_ms(delay)
#             pin.value(0)
#             time.sleep_ms(delay)

def turn(pin, turns, delay):
    en_pins[step_pins.index(pin)].low()
    for i in range(int(turns * FULL_TURN)):
        pin.value(1)
        time.sleep_ms(delay)
        pin.value(0)
        time.sleep_ms(delay)
        turn_count[step_pins.index(pin)] += 1

        for count in turn_count:
            if count*FULL_TURN >= MAX_TURN:
                break
    print(turn_count)

print("initialized")


turn(step_pins[0], 1, 2)
en_pins[0].high()
last_status = 'doorOpenn'
status = ''

print('steps done')

# while True:

#     try:
#         response = requests.get(url=url)
#         json_data = response.json()
#         data = json.loads(json_data)
#         status = data["content"]
#     except:
#         pass

#         if status != last_status:
#             last_status = status
#             # close / open windows

