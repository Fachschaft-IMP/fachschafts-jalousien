# # Importiere das socket-Modul
# import socket

# # Erstelle eine socket-Objekt
# client = socket.socket()

# # Verbinde dich mit localhost:3000
# client.connect(("localhost", 3000))

# # Schleife, die auf eingehende Nachrichten wartet
# print("start while true")
# while True:
#     # Erhalte eine Nachricht vom Server
#     message = client.recv(1024)

#     # Gib die Nachricht aus
#     print(message.decode())

import requests

url = "http://localhost:3000/get-volume"
data = {
    "id": "jalou-slider1",
    "volume": 50
}

while True:
    # response = requests.post(url, json=data)
    test = requests.get(url)

    print(test.status_code)
    print(test)