#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h <= 0 || w <= 0) {
      return undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
