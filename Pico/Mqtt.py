from lib.umqtt.simple import MQTTClient
import time

class Mqtt:

    def __init__(self):
        pass
    # MQTT-Konfiguration
    mqttBroker = 'io.adafruit.com'
    mqttClient = 'pico'
    mqttUser = 'FachschaftIMP'
    mqttPW = 'aio_SHsV37ObHftQVPWEnnGnUrSNtx2Z'
    mqttTopic = "FachschaftIMP/feeds/"

    # Funktion: Verbindung zum MQTT-Server herstellen
    def mqttConnect(self):
        if self.mqttUser != '' and self.mqttPW != '':
            print("MQTT-Verbindung herstellen: %s mit %s als %s" % (self.mqttClient, self.mqttBroker, self.mqttUser))
            client = MQTTClient(self.mqttClient, self.mqttBroker, user=self.mqttUser, password=self.mqttPW)
        else:
            print("MQTT-Verbindung herstellen: %s mit %s" % (self.mqttClient, self.mqttBroker))
            client = MQTTClient(self.mqttClient, self.mqttBroker)
        print("connecting to adafruit...")
        try:
            client.connect()
        except:
            with open('Output.txt', mode='a') as file:
                print('MQTT not able to connect %s' % time.time(), file=file)
            
        print()
        print('MQTT-Verbindung hergestellt')
        print()
        return client

    def send(self, feedname, message):
        try:
            client = self.mqttConnect()
            client.publish(self.mqttTopic+feedname, str(message))
            client.disconnect()
        except OSError:
            print()
            print('Fehler: Keine MQTT-Verbindung')

    ## ich weiß nicht, ob das so funktioniert
    def subscribe(self, feednames):
        client = self.mqttConnect()
        for feedname in feednames:
            client.subscribe(str(self.mqttTopic+feedname))

        def handle_incoming_messages(topic, msg):
            print('Received message:', msg, 'on topic:', topic)

        client.set_callback(handle_incoming_messages)