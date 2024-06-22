function capitalize(s){
  let evenArr = [];
  let oddArr = [];
  for(let i = 0; i < s.length; i++){
    if(i % 2 === 0){
     evenArr.push(s[i].toUpperCase());
      oddArr.push(s[i].toLowerCase());
    }else{
      oddArr.push(s[i].toUpperCase());
      evenArr.push(s[i].toLowerCase())
      
    }
  }
   return [evenArr.join(''), oddArr.join('')];
}

//The above solution is done using arrays. Below simply using strings and is much faster.

function capitalize(s){
  let evenStr = '';
  let oddStr = '';
  for(let i = 0; i < s.length; i++){
    if(i % 2 === 0){
     evenStr += s[i].toUpperCase();
      oddStr += s[i].toLowerCase();
    }else{
      oddStr += s[i].toUpperCase();
      evenStr += s[i].toLowerCase();
    }
  }
   return [evenStr, oddStr];
}