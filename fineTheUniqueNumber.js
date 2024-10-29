//function findUniq(arr){
//    let sortedArr = arr.sort((a, b) => a - b);
//    return sortedArr[0] === sortedArr[1] ? sortedArr.pop():sortedArr[0]
//}


function findUniq(arr){
    return arr.find(n => arr.findIndexOf(n) === arr.lastIndexOf(n));
}
//O(n) run time which is more efficient than iterating through the entire array with sort
//Ideally you would stop the search for the different number as soon as you find it rather than
//continuing to search through the array
