function howManySmaller(arr, n){
    return arr.filter(element => +element.toFixed(2) < n).length
}