#!/usr/bin/node

// prints the number of movies where the character “Wedge Antilles” is present

const process = require('process');
const request = require('request');

const useURL = process.argv[2];
const found = [];
const targetName = 'Wedge Antilles';

// fetch the name of a character and return it
const getName = function (character) {
  request.get(character, (err, resp, body) => {
    if (error) { console.error(error); }
    const name = JSON.parse(body).name;
    if (name === targetName) {
      found.push(name);
    }
  });
};

// iterate through the characters in a movie if its the required character
const iterateResults = function (results) {
  for (result of results) {
    for (character of result.characters) {
      getName(character);
    }
  }
};

const fetch = function () {
  request.get(useURL, (error, response, body) => {
    iterateResults(JSON.parse(body).results);
  });
};

fetch();
console.log(found.length);
