function predictAge(age1, age2, age3, age4, age5, age6, age7, age8){
     let ageOne = age1 * age1
 let ageTwo = age2 * age2
 let ageThree = age3 * age3
 let ageFour = age4 * age4
 let ageFive = age5 * age5
 let ageSix = age6 * age6
 let ageSeven = age7 * age7
 let ageEight = age8 * age8
 
 let ageSum = ageOne + ageTwo + ageThree + ageFour + ageFive + ageSix + ageSeven + ageEight
 
 let ageRoot = Math.sqrt(ageSum)
 
 return Math.floor(ageRoot/2)
}


// const predictAge = (...ages) => Math.hypot(...ages) / 2 | 0; WTF