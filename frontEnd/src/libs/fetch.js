import axios from 'axios';
import qs from 'qs';
import Vue from 'vue';

console.log(process)

let service = axios.create({ // 已经是一个promise 了
  baseURL: '/',
  timeout: 30000
});
// POST传参序列化(添加请求拦截器)
service.interceptors.request.use(
  config => {
    // if ( config.method === 'post' || 'put' || 'delete') { // 序列化
    //   config.data = qs.stringify(config.data);
    // }
    return config;
  },
  error => {
    return Promise.reject(error.data.error.message);
  }
);

service.interceptors.response.use(function (response) {
  return response.data;
}, function (error) {
  return Promise.reject(error);
});

Vue.prototype.ajax = service;
export default service;
