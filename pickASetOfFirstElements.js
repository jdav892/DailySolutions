function first(arr, n){
    if(n === undefined){
        return arr.length > 0 ? [arr[0]] : [];
    }else if(n === 0){
        return [];
    }
    return arr.slice(0, n);
}


//function first(arr, n=1){
//    return arr.slice(0, n);
//}