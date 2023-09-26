#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], (reqerr, res, body) => {
  fs.writeFile(process.argv[3], body, 'utf8', (err) => {
    if (err) throw err;
  });
});
