const http = require('http');
const fs = require('fs');
var net = require('net');

const server = http.createServer((req, res) => {
    fs.readFile('Controller/TCP_Senden/send.html', 'utf8', (err, data) => {
        if (err) {
            console.error(err);
            res.statusCode = 500;
            res.end('Server Error');
        } else {
            res.statusCode = 200;
            res.setHeader('Content-Type', 'text/html');
            res.end(data);
        }
    });

    const bodyParser = require('body-parser');
    server.use(bodyParser.urlencoded({ extended: true }));

    server.post('/', (req, res) => {
    console.log(req.body.value);
    res.end('Received value: ' + req.body.value);
});
});

server.listen(3000, '127.0.0.1', () => {
   console.log('Server running at http://127.0.0.1:3000/');
});




