#!/usr/bin/node
function findMaxNum (arr) {
  let max = arr[0];
  for (const i of arr) max = i > max ? i : max;
  return max;
}

function findSecondMaxNum (max, arr) {
  let secMax = arr[0] === max ? arr[1] : arr[0];
  for (const i of arr) secMax = i > secMax && i < max ? i : secMax;
  return secMax;
}

if (process.argv.length <= 3) console.log(0);
else {
  const arrOfNumbers = process.argv.slice(2).map((item) => Number(item));
  // console.log(arrOfNumbers);
  const max = findMaxNum(arrOfNumbers);
  // console.log(max);
  const secMax = findSecondMaxNum(max, arrOfNumbers);
  console.log(secMax);
}
