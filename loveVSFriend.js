function wordsToMarks(string){
 string = string.toUpperCase();
  let sum = 0;
  
  for(let i = 0; i < string.length; i++){
    let char = string.charCodeAt(i);
    
    if(char >= 65 && char <= 90){
      let pos = char  - 64;
      sum += pos;
    }
  }
  return sum;
}