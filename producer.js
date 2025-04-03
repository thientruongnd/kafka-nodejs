const express = require('express');
const { producer } = require('./kafka');

const router = express.Router();

router.post('/send', async (req, res) => {
  const { message } = req.body;

  try {
    await producer.connect();
    await producer.send({
      topic: 'demo-topic',
      messages: [{ value: message }],
    });
    await producer.disconnect();

    res.json({ success: true, message: 'Message sent to Kafka' });
  } catch (err) {
    console.error('Error sending message:', err);
    res.status(500).json({ success: false, error: err.message });
  }
});

module.exports = router;
