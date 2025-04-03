import os

FILES = {
    "package.json": '''
{
  "name": "kafka-demo",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "consumer": "node consumer.js"
  },
  "dependencies": {
    "express": "^4.18.2",
    "kafkajs": "^2.2.4"
  }
}
''',

    "kafka.js": '''
const { Kafka } = require('kafkajs');

const kafka = new Kafka({
  clientId: 'demo-app',
  brokers: ['localhost:9092'],
});

const producer = kafka.producer();
const consumer = kafka.consumer({ groupId: 'demo-group' });

module.exports = { kafka, producer, consumer };
''',

    "producer.js": '''
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
''',

    "consumer.js": '''
const { consumer } = require('./kafka');

const runConsumer = async () => {
  await consumer.connect();
  await consumer.subscribe({ topic: 'demo-topic', fromBeginning: true });

  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      console.log(`📥 Received message: ${message.value.toString()}`);
    },
  });
};

runConsumer().catch(console.error);
''',

    "index.js": '''
const express = require('express');
const producerRoute = require('./producer');

const app = express();
app.use(express.json());

app.use('/', producerRoute);

app.listen(3000, () => {
  console.log('🟢 Server running at http://localhost:3000');
});
'''
}

def main():
    for filename, content in FILES.items():
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Created/Updated {filename}")

    print("\n✅ Các file dự án đã được tạo trong thư mục hiện tại.")
    print("👉 Các bước tiếp theo:")
    print("   npm install")
    print("   npm run start      # Chạy Express server")
    print("   npm run consumer   # Chạy Kafka consumer")

if __name__ == "__main__":
    main()
