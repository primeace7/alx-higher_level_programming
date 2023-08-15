#!/usr/bin/node

function add (a, b) {
  a = Number(a);
  b = Number(b);

  return (a + b);
}

console.log(add(process.argv[2], process.argv[3]));
