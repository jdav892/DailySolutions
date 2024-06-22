var countSheep = function (num){
    if(num === 0){
      return ""
    }
    
    let sheepCount = ""
    for(let i = 1; i <= num; i++){
      sheepCount += `${i} sheep...`
    }
    return sheepCount
  }