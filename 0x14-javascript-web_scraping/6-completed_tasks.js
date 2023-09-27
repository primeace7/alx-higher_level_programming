#!/usr/bin/node
// computes the number of tasks completed by user id

const request = require('request');
const process = require('process');

const url = process.argv[2];
const output = {};

const countTasks = function (allTasks) {
  for (const task of JSON.parse(allTasks)) {
    if (output[task.userId] && task.completed === true) {
      output[task.userId] += 1;
    } else if (task.completed === true) {
      output[task.userId] = 1;
    }
  }
  console.log(output);
};

// get webpage content and save to file
request.get(url, (error, response, body) => {
  if (error) { console.error(error); }
  countTasks(response.body);
});
