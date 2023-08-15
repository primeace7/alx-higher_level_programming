#!/usr/bin/node

if (typeof BigInt(process.argv[2]) === 'bigint') {
  console.log(`My number: ${process.argv[2]}`);
} else {
  console.log('Not a number');
}
