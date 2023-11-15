import express from 'express';
import fs from 'fs';
const app = express();

app.use(express.static('public'));



app.post('/control', express.json(), (req, res) => {
  const action = req.body.action;
  if (action === 'set-volume') {
    const volume = req.body.volume;
    loudness.setVolume(volume)
      .then(() => res.send('Volume set'))
      .catch(err => {
        console.error(`Failed to set volume: ${err.message}`);
        res.status(500).send('Failed to set volume');
      });
  }
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
