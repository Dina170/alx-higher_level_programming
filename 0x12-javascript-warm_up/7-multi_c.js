#!/usr/bin/node

const stop = parseInt(process.argv[2]);

if (stop) {
  for (let i = 0; i < stop; ++i) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
