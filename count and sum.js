function countPositivesSumNegatives(input){
   if(input == null || input.length == 0){
    return []
   }
    let positive = 0;
    let negative = 0;
    
    for(let i = 0; i <= input.length; i++){
        if (input[i] > 0){
            positive ++;   
    }else if(input [i] < 0){
            negative += input[i];
        }
    }
    return [positive, negative]
}
