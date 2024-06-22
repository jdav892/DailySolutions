function sumMix(x){
    let sum = x.map(num => parseInt(num, 10));
    return sum.reduce((acc, c) => acc + c, 0)
}