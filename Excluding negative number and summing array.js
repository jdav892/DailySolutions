function positiveSum(arr){
    arr.filter(arr => arr > 0)
    return arr.reduce((a, b) => a + b, 0)
}

//function positiveSum(arr) { 
//    return arr.filter(x => x >=0).reduce((a, c) => a + c, 0);
//}
// above was the cleanest solution presented.