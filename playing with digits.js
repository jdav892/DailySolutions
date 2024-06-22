function digPow(n, p){
    let sum = 0;
    let numString = n.toString();
    
    for(let i = 0; i < numString.length; i++){
        sum += Math.pow(parseInt(numString[i], 10), p + i);
    }
    return sum % n === 0 ? sum / n : -1;
}