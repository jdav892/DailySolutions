var maxSequence = function(arr){
  let mSum = 0;
  let currSum = 0;
  
  for(let i = 0; i < arr.length; i++){
    currSum = Math.max(arr[i], currSum + arr[i])
    mSum = Math.max(currSum, mSum)
  }
  return mSum
}