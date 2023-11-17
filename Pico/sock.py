import usocket
import ujson

# Set up the socket connection
s = usocket.socket()
addr = usocket.getaddrinfo("localhost", 3000)[0][-1]
s.bind(addr)
s.listen(1)

# Wait for a connection
conn, addr = s.accept()
print('Connection from:', addr)

# Receive data from the client
data = conn.recv(1024)
data = ujson.loads(data)
print('Received data:', data)

# Close the connection
conn.close()
s.close()