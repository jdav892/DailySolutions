 function findMultiples(integer, limit){
    let mults = [];
    for(let i = 1; i <= limit; i++){
        if(i % integer === 0){
            mults.push(i)
        }
    }
    return mults
 }
