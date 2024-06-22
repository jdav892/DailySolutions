function sumTwoSmallestNumbers(numbers) {  
  let order = numbers.sort((a, b) => a - b);
  let sum = order.splice(0, 2).reduce((acc, c) => acc + c, 0);
  
  return sum;
}

//function sumTwoSmallestNumbers(numbers){
//    let order = numbers.sort((a, b) => a - b);
//
//   return order[0] + order[1];
//}