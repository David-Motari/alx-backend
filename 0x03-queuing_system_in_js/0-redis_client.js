import { createClient } from 'redis'; // importing redis_node module createClient function

const client = createClient(); // Creating client

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`); // output incase of errror
});

client.on('ready', () => {
    console.log('Redis client connected to the server'); // output on connection
});
