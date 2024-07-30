function openOrSenior(data){
    let arrOut = [];
    for(let i = 0; i < data.length; i++){
      if(data[i][0] >= 55 && data[i][1] > 7){
        arrOut.push('Senior')
      }else{
        arrOut.push('Open')
      }
    }return arrOut
  }