import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const data = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
};

for (const keys in data) {
  client.HSET('HolbertonSchools', keys, data[keys], (err, reply) => {
    if (err) { throw (err); } else { console.log(reply); }
  });
}
client.HGETALL('HolbertonSchools', (err, reply) => {
  if (err) { throw (err); } else { console.log(reply); }
});
