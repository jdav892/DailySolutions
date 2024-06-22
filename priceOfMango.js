function mango(quantity, price){
let mangoC = 0;
  for(let i = 1; i <= quantity; i++){
    if(i % 3 === 0){
      mangoC ++
    }
  }
  
  if(quantity <= 2){
    return quantity*price
  }else{
    return (quantity - mangoC) * price
  }
 }


 //function mango(quantity, price){
 // return price*(quantity - Math.floor(quantity/3));
 //}