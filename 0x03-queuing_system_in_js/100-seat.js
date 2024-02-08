import { createClient } from 'redis';
import { promisify } from 'util';
import { createQueue } from 'kue';
import express from 'express';

const client = createClient();

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

setAsync('available_seats', 50);

let reservationEnabled = true;

async function reserveSeat (number) {
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats () {
  const availableSeats = await getAsync('available_seats');
  return parseInt(availableSeats) || 0;
}

const queue = createQueue();
const app = express();
const port = 1245;

app.get('/available_seats', async (req, res) => {
  try {
    const availableSeats = await getAsync('available_seats');
    res.status(200).json({ availableSeats: parseInt(availableSeats) || 0 });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
}).get('/reserve_seat', async (req, res) => {
  try {
    if (!reservationEnabled) {
      return res.status(200).json({ status: 'Reservation are blocked' });
    }

    const kueJob = queue.create('reserve_seat', {});

    kueJob.on('enqueue', () => {
      console.log('Reservation in process');
    }).on('complete', () => {
      console.log(`Seat reservation job ${kueJob.id} completed`);
    }).on('failed', (err) => {
      console.error(`Seat reservation job ${kueJob.id} failed: ${err}`);
    });

    kueJob.save();
    res.status(200).json({ status: 'Reservation in process' });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ status: 'Reservation failed' });
  }
}).get('/process', async (req, res) => {
  try {
    console.log('Queue processing');
    queue.process('reserve_seat', async (job, done) => {
      try {
        const currentAvailableSeats = await getCurrentAvailableSeats();
        if (currentAvailableSeats === 0) {
          reservationEnabled = false;
          done(new Error('Not enough seats available'));
        } else {
          reserveSeat(currentAvailableSeats - 1);
          if (currentAvailableSeats - 1 === 0) {
            reservationEnabled = false;
          }
          done();
        }
      } catch (error) {
        console.error('Error processing queue:', error);
        done(error);
      }
    });
    res.status(200).json({ status: 'Queue processing' });
  } catch (error) {
    res.status(500).json({ status: 'Error processing queue' });
  }
});

app.listen(port, () => {
  console.log(`server is running on ${port}`);
});
