function reverseWords(str){
    return str.replace(/\S+/g, function(word){
        return word.split('').reverse().join('')
    });
}



//function reverseWords(str) {
//  // Go for it
//  //split words into seperate arrays
//  return str.split("").reverse().join("").split(" ").reverse().join(" ");
//}