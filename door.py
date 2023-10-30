import sys
import time
import ntptime
import machine
import network
import urequests as requests

# Wi-Fi-Verbindung herstellen
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("Fachschaft IMP", "8clFBb:oR;Q/#scBBj")  # SSID und Passwort anpassen

while not wifi.isconnected():
    pass


# Watchdog inizialisieren
wtd = machine.WDT()

base_url = 'http://192.168.1.241:8000/?content='
# Schalter an Pin GP14 konfigurieren
sensor_pin = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin("LED")

last_sensor_state = "doorOpen"

start_timer_request = time.time()
start_timer_reset = time.time()
request_duration = 60 * 60 # 60 minutes
reset_duration = 12 * 60 * 60 # 24 hours



while True:
    # Schalterzustand überprüfen
    sensor_state = "doorOpen" if sensor_pin.value() else "doorClosed"
    print(sensor_state) 

    # Wenn sich der Schalterzustand ändert
    if sensor_state != last_sensor_state:
        last_sensor_state = sensor_state
        
        url = base_url + sensor_state
        # print(url)
        try:
            print("response succsess")
            response = requests.get(url=url)
        except:
            print("An exception occurred")
            with open("Output.txt", "a") as text_file:
                print("request failed %s" % time.localtime(), file=text_file)
        # response = requests.get(base_url + sensor_state)

        led.toggle()
        # print("change")
        for i in range(5):
            wtd.feed()
            time.sleep(2)


    # Timer hochzählen lassen
    current_time = time.time()
    elapsed_time_request = current_time - start_timer_request
    elapsed_time_reset   = current_time - start_timer_reset

    # Jede 60 Minuten die Seite aufrufen, sodass sie nicht down geht
    if elapsed_time_request >= request_duration:
        url = base_url + sensor_state
        try:
            response = requests.get(url=url)
        except:
            with open("Output.txt", "a") as text_file:
                text_file.write("request failed in elapsed_time %s" % time.localtime())
        start_timer_request = current_time

    if elapsed_time_reset >= reset_duration:
        sys.exit()
        start_timer_reset = current_time

    wtd.feed()
    
    time.sleep(2)