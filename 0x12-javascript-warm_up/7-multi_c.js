#!/usr/bin/node
let n = Number(process.argv[2]);
if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else if (n <= 0) {
  // Do nothing
} else {
  n = Math.floor(n);
  while (n--) {
    console.log('C is fun');
  }
}
