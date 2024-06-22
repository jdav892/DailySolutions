function dutyFree(normPrice, discount, hol){
//Arithmetic to find solution; hol dividded by the number of bottles after discount applied which is discount/100 in test cases due to no decimals.
//Math.floor solution to not have a floating point number as well as being round down.
  let totalReturn =  hol / (normPrice * (discount/100))
  
  return Math.floor(totalReturn)
}