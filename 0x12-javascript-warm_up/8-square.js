#!/usr/bin/node

const input = process.argv[2];
try {
  if (typeof input === 'undefined') {
    console.log('Missing size');
  } else {
    BigInt(input);
    for (let i = 0; i < input; i++) {
      for (let j = 0; j < input; j++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
} catch {
  console.log('Missing size');
}
