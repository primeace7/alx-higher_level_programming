#!/usr/bin/node

// print all characters of a star wars movie

const process = require('process');
const request = require('request');
const useURL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(useURL, (error, response, body) => {
  if (error) { console.error(error); }
  const charactersList = JSON.parse(body).characters;
  getAge(charactersList);
}
);

// fetches the character's creation date and converts it to time passed
// since the epoch. Older characters will have smaller values
const getAge = function (charactersList) {
  const orderedCharacters = {};
  for (const character of charactersList) {
    request(character, (error, response, body) => {
      if (error) { console.error(error); }
      const name = JSON.parse(body).name;
      const created = new Date(JSON.parse(body).created);
      const age = created.getTime();
      orderedCharacters[age] = name;
    });
  }
  const sortedAge = Object.keys(orderedCharacters).toSorted();
  for (let i = 0; i < orderedCharacters.length; i++) {
    console.log(orderedCharacters[sortedAge[i]]);
  }
};
