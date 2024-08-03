function multiplyAll(arr){
    return function(v){
        return arr.map(num => num * v);
    }
}