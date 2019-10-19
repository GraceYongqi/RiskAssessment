import fetch from '../libs/fetch.js';

export function compute_level_risk (choice = []) {
  let data = {
    "choice" : choice
  }
  return fetch({
    url: '/compute_risk',
    method: 'post',
    data: data
  });
}

export function get_metrics (params = {}) {
  return fetch({
    url: '/indexes',
    method: 'get',
    params: params
  });
}

export function post_metrics (data = {}) {
  return fetch({
    url: '/indexes',
    method: 'post',
    data: data
  });
}

export function post_method (data = {}) {
  return fetch({
    url: '/alarms',
    method: 'post',
    data: data
  });
}