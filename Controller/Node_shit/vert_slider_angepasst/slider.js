// const net = require('net');

// const client = new net.Socket();

// const serverIP = '192.168.0.100'; // IP-Adresse des Servers
// const serverPort = 3000; // Port, auf dem der Server lauscht

const serverURL = 'ws://192.168.0.100:3000'; // URL des WebSocket-Servers

const socket = new WebSocket(serverURL);


document.addEventListener('DOMContentLoaded', function() {
    const slider = document.getElementById('sss');
    const lamellen = document.querySelectorAll('.lamelle');

    const initialPosition = lamellen[0].offsetTop;


    slider.addEventListener('input', function() {
        const value = slider.value;
        let i = 0;
        for (const lamelle of lamellen) {
            lamelle.style.top = initialPosition + (value - slider.min) * (i * lamelle.offsetHeight*0.8) / (slider.max - slider.min) + 'px';
            i++;
        }

        socket.send(value);

    });

    
    socket.addEventListener('open', () => {
        console.log('Connected to server');
      });
      
      socket.addEventListener('message', (event) => {
        console.log('Received:', event.data);
        // Hier kannst du die empfangenen Daten weiterverarbeiten
      });
    
      
      socket.addEventListener('close', () => {
        console.log('Connection closed');
      });
});


// const net = require('net');

// const client = new net.Socket();

// const serverIP = '192.168.0.100'; // IP-Adresse des Servers
// const serverPort = 3000; // Port, auf dem der Server lauscht

// const slider = document.getElementById('slider'); // Annahme: Der Slider hat die ID 'slider'

// slider.addEventListener('input', () => {
//   const value = slider.value;
//   client.connect(serverPort, serverIP, () => {
//     console.log('Connected to server');
//     client.write(value);
//   });
// });

// client.on('data', (data) => {
//   console.log('Received:', data.toString().trim());
//   // Hier kannst du die Bestätigung des Servers weiterverarbeiten
// });

// client.on('close', () => {
//   console.log('Connection closed');
// });


