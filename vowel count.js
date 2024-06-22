function getCount(str) {
    let count = 0;
    for(let i = 0; i < str.length; i++){
      if(str[i] === 'a' || str[i] === 'e' || str[i] === 'i' || str[i] === 'o' || str[i] === 'u')
        count ++;
   }
    return count;
  }

//   function getCount(str){
//     return (str.match(/[aeiou]/ig) || [])
//   }  seemed like a nice one liner to solve this problem.