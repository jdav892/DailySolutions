function multiples(m, n){
    let counterArr = [];
    for(let i = 1; i <= m; i++){
        counterArr.push(n * i);
    }
    return counterArr
}