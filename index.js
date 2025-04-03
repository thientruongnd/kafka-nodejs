const express = require('express');
const producerRoute = require('./producer');

const app = express();
app.use(express.json());

app.use('/', producerRoute);

app.listen(3000, () => {
  console.log('🟢 Server running at http://localhost:3000');
});
