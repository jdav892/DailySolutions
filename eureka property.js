function sumDigPow(a, b){
    const eur = [];
    for(let i = a; i <= b; i++){
        if(isEurNum(i)){
            eur.push(i)
        }
    }
    return eur
}

function isEurNum(n){
    const digits = n.toString().split('').map(Number);
    const sum = digits.reduce((acc, digits, index) => acc + Math.pow(digits, index + 1), 0);
    return sum === n;
}