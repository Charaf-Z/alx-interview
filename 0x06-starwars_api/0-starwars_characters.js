#!/usr/bin/node

const request = require("request");

request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  function (err, res, body) {
    if (err) throw err;
    printActor(JSON.parse(body).characters, 0);
  },
);

function printActor(actors, idx) {
  if (idx === actors.length) return;
  request(actors[idx], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    printActor(actors, idx + 1);
  });
}
