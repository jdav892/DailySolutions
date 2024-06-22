function duplicateCount(text){
    text = text.toLowerCase();
    let input = new Set();
    let doubles = new Set();

    for(let char of text){
        if(char.match(/[a-z0-9]/i)) {
            if(input.has(char)){
                doubles.add(char);
            }else{
                input.add(char);
            }
        }
    }
    return doubles.size

}
// function duplicateCount(text){
//     return (text.toLowerCase().split('').sort().join('').match(/([^])\1+/g) || []).length;
//   }