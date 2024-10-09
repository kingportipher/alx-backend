import redis from 'redis';

// Create Redis client
const client = redis.createClient();

// Handle error events
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

// Handle successful connection
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Store hash values in Redis
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// Display the stored hash values
client.hgetall('HolbertonSchools', (err, result) => {
    if (err) {
        console.error('Error retrieving the hash:', err);
    } else {
        console.log(result);
    }
});
