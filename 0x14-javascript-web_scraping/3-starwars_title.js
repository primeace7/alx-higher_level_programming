#!/usr/bin/node

// print title of a Star Wars movie where the episode number matches a given integer

const process = require('process');
const request = require('request');

const useURL = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];

request.get((useURL), (error, response, body)=>{
    console.log(JSON.parse(body).title);
});
