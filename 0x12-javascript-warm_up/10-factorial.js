#!/usr/bin/node

function factorial (num) {
  if (isNaN(num) || num === 0) { return 1; } else {
    return num * factorial(num - 1);
  }
}

const number = Number(process.argv[2]);
console.log(factorial(number));
