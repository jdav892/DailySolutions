function getSum (a, b)
{ 
  if(a == b){
    return a;
  }else if(a < b){
    return a + getSum(a + 1 , b);
  }else{
    return a + getSum(a - 1, b);
  }
}

// const getSum = (a, b) => {
//     let min = Math.min(a, b);
//     let max = Math.max(a, b);

//     return (max - min + 1) * (min + max / 2)
// }            I would consider this ideal compared to my initial solution