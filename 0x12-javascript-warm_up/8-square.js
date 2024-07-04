#!/usr/bin/node
const squareSize = Number(process.argv[2]);
if (isNaN(squareSize) === true) console.log('Missing size');
else {
  let square = '';
  for (let i = squareSize; i > 0; i--) {
    for (let j = squareSize; j > 0; j--) {
      square += 'X';
    }
    if (i === 1) continue;
    square += '\n';
  }
  console.log(square);
}
