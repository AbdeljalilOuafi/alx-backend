#!/usr/bin/node

import redis from 'redis';

const client = redis.createClient();
const hashKey = "HolbertonSchools";

client.on('connect', () => {
  console.log('Redis client conneced to the Server');
});

client.on('error', (err) => {
  console.log(`Redis client Failed to connect to the Server: ${err}`);
});

client.hset(hashKey, "Portland", 50, redis.print);
client.hset(hashKey, "Seattle", 80, redis.print);
client.hset(hashKey, "New York", 20, redis.print);
client.hset(hashKey, "Bogota", 20, redis.print);
client.hset(hashKey, "Cali", 40, redis.print);
client.hset(hashKey, "Paris", 2, redis.print);


client.hgetall(hashKey, (err, hash) => {
  if (err) throw err;
  console.log(hash);
});
