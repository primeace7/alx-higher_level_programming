#!/usr/bin/node
const num = process.argv[2];
if (typeof num === 'undefined') {
  console.log('Not a number');
} else {
  BigInt(num);
  console.log(`My number: ${num}`);
}
