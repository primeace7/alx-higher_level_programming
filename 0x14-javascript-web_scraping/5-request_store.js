#!/usr/bin/node
// get the content of a webpage and store it in a file

const request = require('request');
const fs = require('fs');
const process = require('process');

const url = process.argv[2];
const destinationFile = process.argv[3];

// get webpage content and save to file
request.get(url)
  .pipe(fs.createWriteStream(destinationFile));
