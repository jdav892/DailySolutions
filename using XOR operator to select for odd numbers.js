function findOdd(A){
let result = 0;
for (let i = 0; i < A.length; i++) {
    result ^= arr[i];
}
return result;
    
}
//const findOdd = A => A.reduce((result, num) => result ^ num, 0);
