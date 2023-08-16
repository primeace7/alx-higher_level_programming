#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size);
    this.printChar = 'X';
  }

  charPrint (charUse) {
    if (this) {
      if (charUse) {
        this.printChar = 'C';
      }
    }
    for (let i = 0; i < this.height; i++) {
      for (let i = 0; i < this.width; i++) {
        process.stdout.write(this.printChar);
      }
      process.stdout.write('\n');
    }
  }

  print () {
    if (this) {
      for (let i = 0; i < this.height; i++) {
        for (let i = 0; i < this.width; i++) {
          process.stdout.write('X');
        }
        process.stdout.write('\n');
      }
    }
  }

  rotate () {
    if (this) {
      const hold = this.width;
      this.width = this.height;
      this.height = hold;
    }
  }

  double () {
    if (this) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}
module.exports = Square;
