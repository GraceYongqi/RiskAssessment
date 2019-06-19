import fetch from '../libs/fetch.js';

export function compute_level_risk (data = {}) {
  data = {
    "choice_arr" : [1, 1, 1, 1, 1]
  }
  return fetch({
    url: '/',
    method: 'post',
    data: data
  });
}