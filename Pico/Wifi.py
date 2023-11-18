import network

class Wifi:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password

    def connect(self) -> None:
        """
        Connecting to Wifi
        """
        wifi = network.WLAN(network.STA_IF)
        wifi.active(True)
        wifi.connect(self.ssid, self.password)
        print("connecting to wifi...")
        while not wifi.isconnected():
            pass
        print('connected')

import urequests
import json
class request:
    def __init__(self, url):
        self.url = url
        self.data_before = None
    
    def get(self) -> dict | None:
        """
        returning a json from given url if possible. None else
        """
        try:
            response = urequests.get(self.url)
            data_after = response.json()

            if self.data_before != data_after:
                # print('Die Daten haben sich geändert:')
                # print('Nachher:', data_after)
                self.data_before = data_after
                return data_after
            
            return None
        except:
            print("connection lost")
            return None