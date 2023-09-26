#!/usr/bin/node

// write a string from commandline to a file

const process = require('process');
const fs =  require('fs');

const useFile = process.argv[2];
const useString = process.argv[3];

fs.writeFile(
    useFile, useString, encoding='utf-8',
    error=>{
	if(error) console.error(error);
    });
