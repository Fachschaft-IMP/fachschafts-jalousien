var net = require('net');
var sliderValue;

document.getElementById('sliderRange').addEventListener('change', function() {
   sliderValue = this.value;
   console.log(sliderValue);
});

// Erstellen einer TCP-Verbindung
var client = new net.Socket();
client.connect(port, host, function() {
   client.write(sliderValue);
});

client.on('data', function(data) {
   console.log(data.toString());
   client.destroy();
});
