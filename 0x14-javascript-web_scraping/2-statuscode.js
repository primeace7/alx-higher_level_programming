#!/usr/bin/node

// display the status code of a GET request

const process = require('process');
const fs =  require('fs');
const request = require('request');

const useURL = process.argv[2];

try{
    request
    .get(useURL)
    .on('response', response=>console.log(response.statusCode));
}
catch (error){
    console.error(error);
}
