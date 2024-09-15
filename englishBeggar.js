function beggars(values, n){
    const result = [];
    let sum = 0;
    for(let i = 0; i < n; i++){
        sum = 0;
        for(let j = i; j < values.length; j += n){
            sum += values[j]
        }
        result.push(sum)
    }
    return result
}