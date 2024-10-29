function findUniq(arr){
    let sortedArr = arr.sort((a, b) => a - b);
    return sortedArr[0] === sortedArr[1] ? sortedArr.pop():sortedArr[0]
}