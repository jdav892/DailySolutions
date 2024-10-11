function primeFactors(n){
    let result = ""
    let divisor = 2
    const factors = {};

    while(n > 1){
        if(n % divisor === 0){
            factors[divisor] = (factors[divisor] || 0) + 1;
            n /= divisor;
        }else{
            divisor++
        }
    }
    for(const[prime, count] of Object.entries(factors)){
        if(count === 1){
            result += `(${prime})`;
        }else{
            result += `(${prime}**${count})`
        }
    }
    return result
}