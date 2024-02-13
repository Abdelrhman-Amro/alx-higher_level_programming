#!/usr/bin/node
function facto (x) {
  if (x === 0) {
    return (1);
  }
  return (x * facto(x - 1));
}

const n = Number(process.argv[2]);
if (isNaN(n)) {
  console.log(1);
} else {
  console.log(facto(n));
}
