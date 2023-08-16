#!/usr/bin/node

exports.esrever = function (list) {
    let reversed = [];
    let count = 0;
    let len = list.length - 1;

    while(len - count >= 0) {
	reversed[count] = list[len - count];
	count++;
    }
    return reversed;
}
