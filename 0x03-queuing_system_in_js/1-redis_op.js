iimport redis from 'redis';

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

// Function to set a new value for a key in Redis
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

// Function to display the value for a key
function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        if (err) {
            console.error(`Error fetching value for ${schoolName}: ${err}`);
        } else {
            console.log(`${schoolName}: ${reply}`);
        }
    });
}

// Test the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

