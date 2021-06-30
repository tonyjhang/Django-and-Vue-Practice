import axios from 'axios';

const loginSev = async function (url, info) {
  return axios.post(url, info);
};

const register = async function (url, info) {
  return axios.post(url, info);
};

export default {
  loginSev,
  register,
};
