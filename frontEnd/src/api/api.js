import fetch from '../libs/fetch.js';

export function compute_level_risk (choice = []) {
  let data = {
    "choice" : choice
  }
  return fetch({
    url: '/',
    method: 'post',
    data: data
  });
}