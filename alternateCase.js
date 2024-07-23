function alternateCase(s) {
    let newS = ''
    for(let i = 0; i < s.length; i++){
      if(s[i] === s[i].toLowerCase()){
        newS += s[i].toUpperCase()
      }else{
        newS += s[i].toLowerCase()
      }
    }
    return newS
  }