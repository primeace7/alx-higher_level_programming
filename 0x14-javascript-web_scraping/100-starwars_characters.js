#!/usr/bin/node

// print all characters of a star wars movie

const process = require('process');
const request = require('request');

const useURL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(useURL, (error, response, body) => {
  if (error) { console.error(error); }
  const charactersList = JSON.parse(body).characters;
  for (const character of charactersList) { getName(character); }
});

const getName = function (character) {
  request(character, (error, response, body) => {
    if (error) { console.error(error); }
    console.log(JSON.parse(body).name);
  });
};
