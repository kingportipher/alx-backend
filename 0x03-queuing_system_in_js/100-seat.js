import express from 'express';
import redis from 'redis';
import util from 'util';
import kue from 'kue';

// Create Redis client
const client = redis.createClient();
client.on('connect', () => {
    console.log('Redis client connected');
}).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

// Function to reserve seats (set available seats)
async function reserveSeat(number) {
    const setAsync = util.promisify(client.set).bind(client);
    return setAsync('available_seats', number);
}

// Initialize the number of available seats to 50
reserveSeat(50);
let reservationEnabled = true;

// Function to get current available seats
async function getCurrentAvailableSeats() {
    const getAsync = util.promisify(client.get).bind(client);
    return getAsync('available_seats');
}

// Create a Kue queue
const queue = kue.createQueue();

// Create an Express server
const app = express();

// Route to get the number of available seats
app.get('/available_seats', async (req, res) => {
    const seats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats: seats }).end();
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
    if (!reservationEnabled) {
        res.json({ status: 'Reservation are blocked' }).end();
    } else {
        const reserveJob = queue.create('reserve_seat').save((err) => {
            if (!err) {
                res.json({ status: 'Reservation in process' }).end();
            } else {
                res.json({ status: 'Reservation failed' }).end();
            }
        });

        // Handle job completion or failure
        reserveJob.on('complete', () => {
            console.log(`Seat reservation job ${reserveJob.id} completed`);
        }).on('failed', (err) => {
            console.log(`Seat reservation job ${reserveJob.id} failed: ${err}`);
        });
    }
});

// Route to process the seat reservation queue
app.get('/process', (req, res) => {
    res.json({ status: 'Queue processing' }).end();

    queue.process('reserve_seat', async (job, done) => {
        const currentSeats = await getCurrentAvailableSeats();

        if (currentSeats === '0') {
            reservationEnabled = false;  // Disable reservations if no seats left
            done();
        } else if (parseInt(currentSeats) > 0) {
            await reserveSeat(parseInt(currentSeats) - 1);  // Decrease available seats by 1
            done();
        } else {
            done(new Error('Not enough seats available'));  // Fail if seats are insufficient
        }
    });
});

// Start the Express server on port 1245
app.listen(1245, () => {
    console.log('Server is listening on port 1245');
});

