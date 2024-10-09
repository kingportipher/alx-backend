import redis from 'redis';

const client = redis.createClient();

// Handle error events
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

// Handle successful connection
client.on('connect', () => {
    console.log('Redis client connected to the server');
});
