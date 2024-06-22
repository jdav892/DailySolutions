const reverseSeq = n => {
   if(n <= 0){
    return [];
   }else{
    const result = [];
    for (let i = n; i >= i; i--){
        result.push(i);
    }
    return result
   }
}

// const reverseSeq = n =>{
// let arr = [];
// for (let i = n; i > 0; i--){
//     arr.push(i);
// }   return arr;
// };