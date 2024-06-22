var number = function(array){
    if(array.length === 0){
        return [];
    }
    const result = array.map((line, index) => `${index + 1}: ${line}`);
    return result
}


//var number = function(array){
//  return array.map(function(line, index){
//      return(index + 1) + ": " + line;
//  });
//}