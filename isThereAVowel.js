function isVow(a){
  const asciiVowels = {
    97: "a",
    101: "e",
    105: "i",
    111: "o",
    117: "u"
 };
  
  return a.map(num => asciiVowels[num] || num);
}