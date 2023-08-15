#!/usr/bin/node
const count = process.argv[2];
if (typeof count === 'undefined' || typeof BigInt(count) !== 'bigint') {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
