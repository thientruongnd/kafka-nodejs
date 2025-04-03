const { Kafka } = require('kafkajs');

const kafka = new Kafka({
  clientId: 'demo-app',
  brokers: ['127.0.0.1:9092'],
});

const producer = kafka.producer();
const consumer = kafka.consumer({ groupId: 'demo-group' });

module.exports = { kafka, producer, consumer };
