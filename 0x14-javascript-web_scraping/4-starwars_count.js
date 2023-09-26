#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) throw err;
  const results = JSON.parse(body).results;
  let count = 0;
  results.forEach(res => res.characters.forEach((char) => {
    if (char.includes('https://swapi-api.alx-tools.com/api/people/18/')) { return count++; }
  }));
  console.log(count);
});
