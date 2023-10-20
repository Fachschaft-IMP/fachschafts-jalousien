from machine import Pin
import utime
import time
import ntptime
import machine
import network

step = Pin(14, Pin.OUT)
dir  = Pin(14, Pin.OUT)

full_step_sequenz = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
led = machine.Pin("LED")


# CET Time in a tuble like time.gmtime()
# def cettime():
#     try:
#         ntptime.settime()
#     except:
#         pass
    
#     year = time.localtime()[0]       #get current year
#     HHMarch   = time.mktime((year,3 ,(31-(int(5*year/4+4))%7),1,0,0,0,0,0)) #Time of March change to CEST
#     HHOctober = time.mktime((year,10,(31-(int(5*year/4+1))%7),1,0,0,0,0,0)) #Time of October change to CET
#     now=time.time()
#     if now < HHMarch :               # we are before last sunday of march
#         cet=time.localtime(now+3600) # CET:  UTC+1H
#     elif now < HHOctober :           # we are before last sunday of october
#         cet=time.localtime(now+7200) # CEST: UTC+2H
#     else:                            # we are after last sunday of october
#         cet=time.localtime(now+3600) # CET:  UTC+1H
#     return(cet)

# Wi-Fi-Verbindung herstellen
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("Fachschaft IMP", "8clFBb:oR;Q/#scBBj")  # SSID und Passwort anpassen

print("connecting...")

while not wifi.isconnected():
    pass

print("connected")

# Watchdog inizialisieren
wtd = machine.WDT()

start_timer_request = time.time()
start_timer_reset = time.time()
request_duration = 60 * 60 # 60 minutes
reset_duration = 12 * 60 * 60 # 24 hours


i = 0
while i < 10:
    step.value(1)  # Setzt den step auf HIGH
    time.sleep(1)  # Wartet eine Sekunde
    step.value(0)  # Setzt den step auf LOW
    time.sleep(1)  # Wartet eine Sekunde
    i = i + 1