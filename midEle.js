function gimmme(triplet){
    const sorted = triplet.slice().sort((a, b) => a - b);
    const middle = sorted[1];

    const midIndex = triplet.indexOf(middle);

    return midIndex;
}

// This is what I was initially intendeding to implement but failed.
//var gimme = function (inputArray) {
  //let index = 0;
  //let max = Math.max(...inputArray);
  //let min = Math.min(...inputArray);
  //for(let i = 0; i < inputArray.length; i++){
    //if(inputArray[i] !== max && inputArray[i] !== min){        
    //  index = i;
    //}
  //return index;
//};