#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
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
