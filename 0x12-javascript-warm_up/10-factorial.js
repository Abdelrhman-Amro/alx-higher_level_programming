#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) === true || n === 1) return 1;
  else if (isFinite(n) === false) return Infinity;
  else return n * factorial(n - 1);
}
console.log(factorial(Number(process.argv[2])));
