import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
    return;
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const asyncGet = promisify(client.get).bind(client);

async function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) { throw(err); } else { console.log(reply); };
    });
};

async function displaySchoolValue(schoolName) {
    try {
        const value = await asyncGet(schoolName);
        console.log(value);
    } catch (error) {
        console.log(error);
    }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
