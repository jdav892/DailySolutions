function findLongest(array){
  return array.reduce((max, num) => (num.toString().length > max.toString().length ? num : max));
}