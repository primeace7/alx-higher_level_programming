#!/usr/bin/node

let input = process.argv[2];
if (typeof input === 'undefined') { console.log('Missing size'); } else {
  input = BigInt(input);
  for (let i = 0; i < input; i++) {
    for (let j = 0; j < input; j++) {
      process.stdout.write('x');
    }
    process.stdout.write('\n');
  }
}
