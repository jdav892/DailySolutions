function minMax(arr){
    let max = Math.max(...arr);
    let min = Math.min(...arr);
    return [min, max]
}

//the spread operator allows an interable to expand in places where multiple arguments are expected