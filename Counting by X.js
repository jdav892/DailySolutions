//function countBy(x, n){
//    return Array.from(Array(n)).map((_, i) => x * ++i);
//}
//
//console.log(countBy(4, 5))

//Below is what I was truly attempting to use to solve this problem, however the above solution is the ideal one.
function countBy(x, n){
    let z = []
    for(let i = 1; i <=n; i++){
        z.push(x*1);
    }
    return z
}