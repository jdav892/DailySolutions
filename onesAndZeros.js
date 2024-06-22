const binaryArrayToNumber = arr => {
  let binString = arr.join('');
  let decNum = parseInt(binString, 2);
  return decNum;
};

// const binaryArrayToNumber = arr => {
//    return parseInt(arr.join(''), 2)
//}