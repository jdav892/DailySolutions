var isSquare = function(n) {
    for(let i = 0; i * i; i++){
        if(i * i === n){
            return true;
        }
    }
    return false;
}

//var isSquare = function(n){
//   return Math.sqrt(n) % 1 === 0
//}