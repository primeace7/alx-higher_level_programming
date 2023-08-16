#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  let count = 0;
  const len = list.length - 1;

  while (len - count >= 0) {
    reversed[count] = list[len - count];
    count++;
  }
  return reversed;
};
