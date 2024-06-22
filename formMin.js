function minValue(values){
  let sorted = [...new Set(values)].sort((a , b) => a - b);
  return parseInt(sorted.join(''))
}