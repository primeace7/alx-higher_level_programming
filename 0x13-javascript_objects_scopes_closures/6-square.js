#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
    printChar = 'X';
  constructor (size) {
      super(size);
  }

    charPrint(charUse) {
	if (this) {
	    if (charUse) {
            this.printChar = 'C';
        }
        for (let i = 0; i < this.height; i++) {
            for (let i = 0; i < this.width; i++) {
                process.stdout.write(this.printChar);
            }
            process.stdout.write('\n');
        }
	}
    }

    print(){
	if (this) {
	for (let i = 0; i < this.height; i++) {
	    for (let i = 0; i < this.width; i++) {
		process.stdout.write('X');
	    }
	    process.stdout.write('\n');
	}
	}
    }

    rotate() {
	if (this) {
	    let hold = this.width;
	    this.width = this.height;
	    this.height = hold;
	}
    }

    double() {
	if (this) {
	    this.width *= 2;
	    this.height *= 2;
	}
    }
}
module.exports = Square;
