function shorterReverseLonger(a, b){
    let short = ''
    let long = ''
    if(a.length >= b.length){
      short += b
      long += a.split("").reverse().join("")
      return `${short}${long}${short}`
    }else{
      short += a
      long += b.split("").reverse().join("")
      return `${short}${long}${short}`
    }
}