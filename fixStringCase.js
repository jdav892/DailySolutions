function solve(s){
 let upperCount = 0;
 let lowerCount = 0;
  for(let i = 0; i < s.length; i++){
    if(s[i] === s[i].toLowerCase() && s[i] !== s[i].toUpperCase()){
      lowerCount++;
    }else if(s[i] === s[i].toUpperCase() && s[i] !== s[i].toLowerCase()){
      upperCount++;
    }
  }
  if(upperCount > lowerCount){
    return s.toUpperCase();
  }else{
    return s.toLowerCase(); 
  }
}