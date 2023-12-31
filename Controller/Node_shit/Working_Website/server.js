const express = require('express');
const bodyParser = require('body-parser');
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

  if(id === 'master-slider') {
    console.log("master slider erkannt")
    for(key in volumes) {
      volumes[key] = req.body.volume;
    }
  }

  // res.setHeader('Content-Type', 'application/json');
  // res.json({'id': id, 'volume':volumes[id]});


});


// Set slider values on Website on loading
app.get('/get-volume', (req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.json(volumes);
 });

 const port = 5000 // Ändern Sie dies auf einen verfügbaren Port
 
 app.listen(port, () => {
   console.log(`App läuft unter: http://localhost:${port}`)
 })