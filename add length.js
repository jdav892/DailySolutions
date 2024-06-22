function addLength(str) {
    const words = str.split(" ");
    const wordCount = words.map(word => `${word} ${word.length}`);
    
    return wordCount;
  }