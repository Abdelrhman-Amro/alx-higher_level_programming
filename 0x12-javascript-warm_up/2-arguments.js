#!/usr/bin/node

const argsNumber = process.argv.length - 2;
if (argsNumber === 1) console.log('Argument found');
else if (argsNumber > 1) console.log('Arguments found');
else console.log('No argument');
