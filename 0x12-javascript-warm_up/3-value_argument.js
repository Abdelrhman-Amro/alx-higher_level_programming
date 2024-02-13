#!/usr/bin/node
let ln = 0;
while (process.argv[ln] !== undefined) {
  ln++;
}

if (ln === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
