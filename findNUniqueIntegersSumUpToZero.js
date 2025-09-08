/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function(n) {
    let result = []
    if(n % 2 !== 0){
        return result.append(0)
    }

    for(let i = 0; i <= n / 2; i++){
        result.append(i, -i)
    }
    return result

}