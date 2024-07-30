function nthSmallest(arr, pos){
    let newArr = arr.split().sort((a, b) => a - b);
    return newArr[pos - 1]
}