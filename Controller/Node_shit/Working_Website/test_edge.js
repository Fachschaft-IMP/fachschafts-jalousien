const express = require('express');
const bodyParser = require('body-parser');
const app = express();

var mqtt = require('mqtt')

var client  = mqtt.connect('mqtt://io.adafruit.com', {
    username: 'FachschaftIMP',
    password: 'aio_Ctis30PsIabbtFm3mlOYTsHuudkg'
})


client.on('error', (err) => {
    console.error('Verbindungsfehler:', err)
})
  
  
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
client.on('connect', function () {
    console.log('Connected to MQTT broker');
  
    // POST route to receive slider value
    app.post('/set-volume', (req, res) => {
        let id = req.body.id;
        volumes[id] = req.body.volume;
        console.log('Received volume:', volumes[id], 'on id', id);
        

        // Ändern Sie die Werte nach Bedarf
        var topic = 'FachschaftIMP/feeds/'+id
        var message = ''+volumes[id]

        client.publish(topic, message, function (err) {
        if (err) {
            console.error('Fehler beim Veröffentlichen der Nachricht:', err)
        } else {
            console.log('Nachricht veröffentlicht:', message)
        }
        });

        res.sendStatus(200);
    });
  });


// Set slider values on Website on loading
app.get('/get-volume', (req, res) => {
    res.setHeader('Content-Type', 'application/json');
    res.json(volumes);
 });

app.listen(3000, () => {
    console.log('Server started on port http://localhost:3000/');
});