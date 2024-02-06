import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
    return;
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) { throw(err); } else { console.log(reply); };
    });
};

function displaySchoolValue(schoolName) {
    console.log(client.get(schoolName, (err, reply) => {
        if (err) { throw(err); } else { console.log(reply); }
    }))
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
