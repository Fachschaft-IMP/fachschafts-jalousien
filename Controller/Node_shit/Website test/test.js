const express = require('express');
const bodyParser = require('body-parser');
const app = express();

let volume = 0;

// Use body-parser middleware to parse JSON bodies
app.use(bodyParser.json());

// Serving static files from 'public' directory
app.use(express.static('public'));

// POST route to receive slider value
app.post('/set-volume', (req, res) => {
 volume = req.body.volume;
 console.log('Received volume:', volume);
 res.send('Volume received');
});

app.get('/get-volume', (req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.json({ volume: volume });
 });

// app.get('/get-volume', (req, res) => {
//   res.json({ volume: volume });
//  });

app.listen(3000, () => {
 console.log('Server started on port http://localhost:3000/');
});
