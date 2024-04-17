#!/usr/bin/node
/* A script that prints all characters of a Star Wars movie */

const request = require('request');
const movieId = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api';

function getMovieCharacters(movieId) {
    request(`${API_URL}/films/${movieId}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}

if (process.argv.length !== 3) {
  console.log("Usage: ./0-starwars_characters.js <movie_id>");
  process.exit(1);
}

getMovieCharacters(movieId);
