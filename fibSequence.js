/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n){
    let seq = [0, 1]
    for(let i = 2; i <= n; i++){
        let a = seq[n - 1]
        let b = seq[n - 2]

        seq.push(a + b)
    }
    return seq[n]
}