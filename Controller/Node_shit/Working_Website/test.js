const express = require('express');
const bodyParser = require('body-parser');
const net = require('net');
const app = express();

let volumes = {
  "jalou-slider1": 0,
  "jalou-slider2": 0,
  "jalou-slider3": 0,
  "jalou-slider4": 0,
  "jalou-slider5": 0,
  "master-slider": 0
 };

// Use body-parser middleware to parse JSON bodies
app.use(bodyParser.json());

// Serving static files from 'public' directory
app.use(express.static('public'));

// POST route to receive slider value
app.post('/set-volume', (req, res) => {
  let id = req.body.id;
  volumes[id] = req.body.volume;
  console.log('Received volume:', volumes[id], 'on id', id);
  
  const data = {
    id: id,
    volume: volumes[id]
  };
 
  const client = net.createConnection({ port: 4000, host: '192.168.1.75' }, () => {
    client.write(JSON.stringify(data)); // Konvertieren Sie das Objekt in eine JSON-Zeichenkette
  });
 
  client.on('end', () => {
    console.log('Verbindung beendet');
    return res.send('Werte gesendet');
  });
 
  return res.send('Volume received');
});


// Set slider values on Website on loading
app.get('/get-volume', (req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.json(volumes);
 });

app.listen(3000, () => {
 console.log('Server started on port http://localhost:3000/');
});