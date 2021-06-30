import axios from 'axios';

const addTraceList = async (url, token) => {
  const headers = {
    'Content-Type': 'application/json',
    Authorization: token,
  };
  return axios.post(`${url}/trace`, headers);
};

const getDetail = async (url, token) => {
  let headers = {
    'Content-Type': 'application/json',
    Authorization: `Token ${token}`,
  };
  return axios.get(url, { headers: headers });
};

const getTraceList = async (url, token) => {
  const headers = {
    'Content-Type': 'application/json',
    Authorization: `Token ${token}`,
  };
  return axios.get(`${url}/trace`, { headers: headers });
};

export default {
  getTraceList,
  getDetail,
  addTraceList,
};
