function powersOfTwo(n){
    let nArr = [];
    for(let i = 0; i <= n; i++){
        let result = 2**i
        nArr.push(result)
    }
    return nArr
}

// function powersOfTwo(n){
//     return Array.from({length: n + 1}, (v, k) => 2 ** k);
// }