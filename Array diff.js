function arrayDiff(a, b) {
  const diff = a.filter((e) => !b.includes(e));
  return diff
}

function diffArrays(b, a) {
  const differ = b.filter((e) => !a.includes(e));
  return differ
}
