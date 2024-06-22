function getDivisorsCnt(n){
    let count = 0;
   for(let i = 1; i <= Math.sqrt(n); i++){
     if(n % i === 0){
       count ++;
     if(n / i !== i){
       count ++;
        }
       }
     }
   return count
 }