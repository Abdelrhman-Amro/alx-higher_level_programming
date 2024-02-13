#!/usr/bin/node
let sz = Number(process.argv[2]);
if (isNaN(sz)) {
  console.log('Missing size');
} else if (sz <= 0) {
  // Do nothing
} else {
  sz = Math.floor(sz);
  for (let i = 0; i < sz; i++) {
    for (let j = 0; j < sz; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
