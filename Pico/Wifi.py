import network

class Wifi:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password

    def connect(self):
        wifi = network.WLAN(network.STA_IF)
        wifi.active(True)
        wifi.connect(self.ssid, self.password)
        print("connecting to wifi...")
        while not wifi.isconnected():
            pass
        print('connected')