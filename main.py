import sys
import time
import ntptime
from machine import Pin
from machine import WDT
import network
import json
import urequests as requests

# Wi-Fi-Verbindung herstellen
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("Fachschaft IMP", "8clFBb:oR;Q/#scBBj")  # SSID und Passwort anpassen

while not wifi.isconnected():
    pass


# Watchdog inizialisieren
wtd = WDT()

url = 'http://192.168.1.241:8000/'
# Schalter an Pin GP14 konfigurieren

step_pins  = [Pin(0, Pin.OUT), Pin(3, Pin.OUT), Pin(6, Pin.OUT), Pin( 9, Pin.OUT), Pin(12, Pin.OUT)]
dir_pins   = [Pin(1, Pin.OUT), Pin(4, Pin.OUT), Pin(7, Pin.OUT), Pin(10, Pin.OUT), Pin(13, Pin.OUT)]
en_pins    = [Pin(2, Pin.OUT), Pin(5, Pin.OUT), Pin(8, Pin.OUT), Pin(11, Pin.OUT), Pin(14, Pin.OUT)]
turn_count = [0, 0, 0, 0, 0]

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

def step(turns, delay):
    for i in range(int(turns * FULL_TURN)):
        for pin in step_pins:
            pin.value(1)
            
        time.sleep_ms(delay)
        for count ,pin in enumerate(step_pins):
            pin.value(0)
            turn_count[count] += 1
        time.sleep_ms(delay)

        for count in turn_count:
            if count*FULL_TURN >= MAX_TURN:
                break

        


step(200, 50)
last_status = 'doorOpenn'
status = ''
while True:

    try:
        response = requests.get(url=url)
        json_data = response.json()
        data = json.loads(json_data)
        status = data["content"]
    except:
        pass

        if status != last_status:
            last_status = status
            # close / open windows

