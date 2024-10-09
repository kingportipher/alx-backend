import redis from 'redis';
import { promisify } from 'util';

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

// Promisify the client.get method
const getAsync = promisify(client.get).bind(client);

// Function to set a new value for a key in Redis
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

// Async function to display the value for a key
async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(`${schoolName}: ${value}`);
    } catch (err) {
        console.error(`Error fetching value for ${schoolName}: ${err}`);
    }
}

// Test the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

