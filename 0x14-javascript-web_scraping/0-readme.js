#!/usr/bin/node

// read and print the content of a file

const process = require('process');
const fs =  require('fs');

fs.readFile(file=process.argv[2], encoding='utf-8', (error, data)=>{
    if (error) {
	console.error(error);
	return;}
    console.log(data);
});
