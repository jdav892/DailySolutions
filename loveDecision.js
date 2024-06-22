function howMuchILoveYou(nbPetals) {
let one = "I love you"
let two  =  "a little"
let three = "a lot"
let four = "passionately"
let five = "madly"
let six = "not at all"

while(nbPetals > 6){
  nbPetals -= 6
    
  }if(nbPetals === 1){
    return one
  }else if(nbPetals === 2){
    return two
  }else if(nbPetals === 3){
    return three
    }else if(nbPetals === 4){
      return four
    }else if(nbPetals === 5){
      return five
    }else{
      return six
    }
  }