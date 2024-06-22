var findAverage = function (nums) {
  let numsArr = [...nums];
  let sum = numsArr.reduce((a, c) => a + c, 0);
  
  return sum/nums.length
}