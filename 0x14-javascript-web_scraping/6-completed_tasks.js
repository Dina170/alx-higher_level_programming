#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) throw err;
  const todos = JSON.parse(body);
  const completedObj = {};

  todos.forEach((todo) => {
    const completed = todo.completed;
    const userId = todo.userId;

    if (completed) {
      if (!completedObj[userId]) {
        completedObj[userId] = 1;
      } else {
        completedObj[userId]++;
      }
    }
  });
  console.log(completedObj);
}
);
