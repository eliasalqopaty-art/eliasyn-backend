const express = require('express');
const app = express();
app.use(express.json());

let shipments = [];

app.get('/', (req, res) => {
  res.send("API is working");
});

app.post('/create-shipment', (req, res) => {
  shipments.push(req.body);
  res.send({ success: true });
});

app.get('/shipments', (req, res) => {
  res.send(shipments);
});

app.listen(3000, () => console.log("Server running"));
