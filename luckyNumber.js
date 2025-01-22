function isLucky(n) {
    let check = 0;
    let numArr = n.toString().split("")
    for(let i = 0; i < numArr.length; i++){
     check += Number(numArr[i])
    }
    if(check == 0 || check % 9 === 0){
      return true
    }
    return false
  
  }