//function findShort(s){            This was an answer from ChatGPT that was satisfactory to complete the question but not what I was looking for to keep for myself.
//    const words = s.split(' ')
//    let minLength = Number.MAX_SAFE_INTEGER;
//    
//    for (const word of words){
//        const currentLength = word.length;
//        if(currentLength < minLength){
//            minLength = currentLength;
//        }
//    }
//    return minLength;
//  }

  const inputString = "What does one consider fruitful action";
  const shortestLength = findShort(inputString);
  console.log(shortestLength)


  
function findShort(s){
    return Math.min(...s.split(" ").map (s => s.length));
}