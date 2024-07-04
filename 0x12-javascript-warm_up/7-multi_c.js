#!/usr/bin/node

const nTimes = process.argv[2];

if (nTimes === undefined) console.log('Missing number of occurrences');
for (let i = Number(nTimes); i > 0; i--) console.log('C is fun');
