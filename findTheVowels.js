function vowelIndices(word){
  let count = [];
 for(let i = 0; i < word.length; i++){
   if(word[i] === 'a' || word[i] === 'e'|| word[i] === 'i' || word[i] === 'o' || word[i] === 'u' || word[i] === 'y' || word[i] === 'A' || word[i] === 'E'|| word[i] === 'I' || word[i] === 'O' || word[i] === 'U' || word[i] === 'Y'){
     count.push(i + 1);
   }
 }
    return count
}