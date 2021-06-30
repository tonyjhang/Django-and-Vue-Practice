export function getTraceList(state) {
  return state.traceList;
}

export function getDetail(state) {
  return state.traceDetail;
}

export function getAmout(state) {
  let result = [
    { name: 'buy', data: [] },
    { name: 'sell', data: [] },
  ];
  state.TraceAmout.forEach((amout) => {
    if (amout >= 0) {
      result[0].data.push(amout);
    } else {
      result[1].data.push(amout);
    }
  });
  return result;
}
