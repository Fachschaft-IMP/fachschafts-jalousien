const http = require('http');
const fs = require('fs');
const url = require('url');

const server = http.createServer(function (req, res) {
  const q = url.parse(req.url, true);
  let filename = "." + q.pathname;
  if (filename === './') {
    filename = './Controller/TCP_Senden/send.html';
  }
  fs.readFile(filename, function(err, data) {
    if (err) {
      res.writeHead(404, {'Content-Type': 'text/html'});
      return res.end("404 Not Found");
    }  
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    const slider1 = q.query.slider1;
    const slider2 = q.query.slider2;
    const slider3 = q.query.slider3;
    const slider4 = q.query.slider4;
    const slider5 = q.query.slider5;
    console.log(`Slider 1: ${slider1}, Slider 2: ${slider2}, Slider 3: ${slider3}, Slider 4: ${slider4}, Slider 5: ${slider5}`);
    return res.end();
  });
});

server.listen(3000, '127.0.0.1', () => {
    console.log('Server running at http://127.0.0.1:3000/');
 });
