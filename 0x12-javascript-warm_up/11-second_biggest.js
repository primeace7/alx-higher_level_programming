#!/usr/bin/node

if (process.argv.length <= 3) { console.log(0); } else {
    let argArray = process.argv.slice(2).toSorted();
    argArray.forEach(elem => BigInt(elem));
  console.log(argArray[argArray.length - 2]);
}
