#!/usr/bin/node

if (process.argv.length <= 3) { console.log(0); } else {
  const argArray = process.argv.slice(2).toSorted();
  console.log(argArray[argArray.length - 2]);
}
