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

led = Pin("LED")

url = 'http://192.168.1.241:8000/'

FULL_TURN = 200
MAX_TURN = 10 * FULL_TURN

step_pins  = [Pin(0, Pin.OUT)]
dir_pins   = [Pin(1, Pin.OUT)]
en_pins    = [Pin(2, Pin.OUT)]
step_count = [0]
MAX_TURNS = [10*FULL_TURN]
# step_pins  = [Pin(0, Pin.OUT), Pin(3, Pin.OUT), Pin(6, Pin.OUT), Pin( 9, Pin.OUT), Pin(12, Pin.OUT)]
# dir_pins   = [Pin(1, Pin.OUT), Pin(4, Pin.OUT), Pin(7, Pin.OUT), Pin(10, Pin.OUT), Pin(13, Pin.OUT)]
# en_pins    = [Pin(2, Pin.OUT), Pin(5, Pin.OUT), Pin(8, Pin.OUT), Pin(11, Pin.OUT), Pin(14, Pin.OUT)]
# step_count = [0, 0, 0, 0, 0]


def turn_on_motor(en_pin):
    en_pin.low()

def turn_off_motor(en_pin):
    en_pin.high()

def switch_dir(dir_pins:Pin, dir:int):
    dir_pins.value(dir)

def step(step_pin, steps, delay_ms):
    idx = step_pins.index(step_pin)
    if idx not in range(0, len(step_pins)):
        return
    # enable Motor
    turn_on_motor(en_pins[idx])
    for i in range(int(steps)):
        step_pin.high()
        time.sleep_ms(delay_ms)
        step_pin.low()
        time.sleep_ms(delay_ms)
        step_count[idx] += 1

        if step_count[idx]*FULL_TURN >= MAX_TURNS[idx]:
            return
    # disable motor
    turn_off_motor(en_pins[idx])

def full_turn(step_pin, turns, delay_ms):
    # getting index of step_pin in Step_pins array
    idx = step_pins.index(step_pin)
    if idx not in range(0, len(step_pins)):
        return
    # enable Motor
    turn_on_motor(en_pins[idx])
    for i in range(int(turns * FULL_TURN)):
        step_pin.high()
        time.sleep_ms(delay_ms)
        step_pin.low()
        time.sleep_ms(delay_ms)
        step_count[idx] += 1

        if step_count[idx]*FULL_TURN >= MAX_TURNS[idx]:
            return

    # disable motor
    turn_off_motor(en_pins[idx])


print("initialized")


full_turn(step_pins[0], 1, 2)
en_pins[0].high()
print('steps done')


# last_status = 'doorOpenn'
# status = ''


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

