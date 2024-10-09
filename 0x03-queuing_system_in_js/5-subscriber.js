import redis from 'redis';

// Create Redis client
const client = redis.createClient();

// Handle connection and error events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

// Subscribe to the 'holberton school channel'
client.subscribe('holberton school channel');

// Handle incoming messages on the subscribed channel
client.on('message', (channel, message) => {
    if (channel === 'holberton school channel') {
        if (message === 'KILL_SERVER') {
            console.log(message);
            client.unsubscribe('holberton school channel');
            client.quit();
        } else {
            console.log(message);
        }
    }
});
