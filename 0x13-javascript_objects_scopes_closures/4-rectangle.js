#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!h || h <= 0 || !w || w <= 0) {
      return undefined;
    } else {
      this.width = w;
      this.height = h;
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
module.exports = Rectangle;
