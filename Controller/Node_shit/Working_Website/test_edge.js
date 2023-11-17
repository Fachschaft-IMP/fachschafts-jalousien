const express = require('express');
const bodyParser = require('body-parser');
const http = require('http');
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
  
  const data = JSON.stringify({
    id: id,
    volume: volumes[id]
  });

  var options = {
    hostname: '192.168.1.211', // Ersetzen Sie dies durch die IP-Adresse Ihres MicroPython-Geräts
    port: 8000,
    path: '/',
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Content-Length': data.length
    }
  };

  var req = http.request(options, (res) => {
    console.log(`statusCode: ${res.statusCode}`);

    res.on('data', (d) => {
      process.stdout.write(d);
    });
  });

  req.on('error', (error) => {
    console.error(error);
  });

  req.write(data);
  req.end();

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
