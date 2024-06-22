function spinWords(string){
  let result = "";
  if(string.length >= 4){
    let line = string.split("\n");
    for(let i = 0; i < line.length; i++){
        let words = lines[i].split(" ");

        for(let j = 0; j < words.length; j++){
            if(words[j].length >= 5){
                words[j] = words[j].split("").reverse().join("");
            }
        }
        result += words.join(" ")
      }
    }
    return result;
}

// function spinWords(words){
//     return words.split(' ').map(function (word) {
//       return (word.length > 4) ? word.split('').reverse().join('') : word;
//     }).join(' ');
//   }