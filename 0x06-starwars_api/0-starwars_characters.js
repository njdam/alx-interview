#!/usr/bin/node
/* A script that prints all characters of a Star Wars movie */

const request = require('request');
const movieId = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/';

function getMovieCharacters(movieId) {
  const url = `${API_URL}/films/${movieId}/`;
  request(url, function(error, response, body) {
    if (!error && response.statusCode == 200) {
      const filmData = JSON.parse(body);
      const characters = filmData.characters;
      characters.forEach(function(characterUrl) {
        request(characterUrl, function(error, response, body) {
          if (!error && response.statusCode == 200) {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          } else {
            console.log(`Failed to fetch character data for ${characterUrl}`);
          }
        });
      });
    } else {
      console.log(`Failed to fetch film data for movie ID: ${movieId}`);
    }
  });
}

if (process.argv.length !== 3) {
  console.log("Usage: ./0-starwars_characters.js <movie_id>");
  process.exit(1);
}

getMovieCharacters(movieId);
