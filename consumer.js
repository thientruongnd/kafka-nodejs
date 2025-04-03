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
