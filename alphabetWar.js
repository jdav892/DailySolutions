function alphabetWar(fight)
{
  
    let right = 0;
    let left = 0;
    let rightVal = {'z': 1, 'd': 2, 'q': 3, 'm': 4}
    let leftVal= {'s': 1, 'b': 2, 'p': 3, 'w': 4}
    for(let i = 0; i < fight.length; i++){
      if(rightVal[fight[i]]){
        right += rightVal[fight[i]]
      }else if(leftVal[fight[i]]){
        left += leftVal[fight[i]]
      }
     }if(right > left){
          return "Right side wins!"
        }else if(left > right){
          return "Left side wins!"
        }else{
          return "Let's fight again!"
      }
    }