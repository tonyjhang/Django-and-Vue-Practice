export function setToken(state, info) {
  state.token = info.data.token;
}

export function setTraceList(state, info) {
  let traceList = [];
  info.data.trace_list.forEach((stock) => {
    traceList.push(stock.stock_num);
  });
  state.traceList = traceList;
}

export function setDetail(state, detail) {
  state.traceDetail = [];
  state.TraceAmout = [];
  state.traceDetail = detail;
  detail.forEach((data) => {
    state.TraceAmout.push(data.total);
  });
}
