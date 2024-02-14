#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arrNumbers = process.argv.slice(2).sort(function (a, b) { return a - b; });
  console.log(arrNumbers[arrNumbers.length - 1]);
}
