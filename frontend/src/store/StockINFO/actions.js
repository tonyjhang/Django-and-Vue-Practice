import trace from 'src/api/stock/trace';
import login from '../../api/login';

export function loginServer({ state, commit }, info) {
  return new Promise((resolve, reject) => {
    login.loginSev(`${state.apiURL}/login`, info)
      .then((loginResult) => {
        commit('setToken', loginResult);
        trace.getTraceList(state.apiURL, state.token)
          .then((traceResult) => {
            commit('setTraceList', traceResult);
            resolve();
          })
          .catch((err) => reject(err));
      })
      .catch((err) => reject(err));
  });
}

export function register({ state }, info) {
  return new Promise((resolve, reject) => {
    login.register(`${state.apiURL}/login`, info)
      .then(() => resolve())
      .catch((err) => reject(err));
  });
}

export async function getDetail({ state, commit }, info) {
  return new Promise((resolve, reject) => {
    if (info.stockNum === '' || info.date === '') {
      return;
    }
    try {
      let url = `${state.apiURL}/stock/${info.stockNum}/date/${info.date}`;
      trace.getDetail(url, state.token)
        .then((res) => {
          if (res.data.count < 20) {
            commit('setDetail', res.data.results);
          } else if (res.data.count < 100 && res.data.count > 20) {
            let result = res.data.results.slice(0, 10)
              .concat(res.data.results.slice(-10));
            commit('setDetail', result);
          } else if (res.data.count > 100) {
            let lastPage = parseInt(res.data.count / 100, 10);
            let firstPageResult = res.data.results.slice(0, 10);
            trace.getDetail(`${url}?page=${lastPage}`, state.token)
              .then((lastRes) => {
                let data = firstPageResult.concat(lastRes.data.results.slice(-10));
                commit('setDetail', data);
              })
              .catch((err) => { reject(err); });
          } else {
            resolve();
          }
        })
        .catch((err) => { reject(err); });

      resolve();
    } catch (err) {
      reject(err);
    }
  });
}
