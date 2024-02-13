#!/usr/bin/node
const firstArg = Number(process.argv[2]);
if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  const n = Math.floor(firstArg);
  console.log('My number: ' + n);
}
