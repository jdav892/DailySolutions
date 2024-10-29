function validBraces(s){
    const stack = []
    const braceMap = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    };
    const openingBrackets = ['(', '[', '{'];
    const closingBrackets = [')', ']', '}'];

    for(let char of s){
        if(openingBrackets.includes(char)){
            stack.push(char);
        }else if(closingBrackets.includes(char)){
            if(stack.length === 0 || stack.pop() !== braceMap[char]){
                return false;
            }
        }
    }
    return stack.length === 0;

}

console.log(validBraces("()"));
console.log(validBraces("{}{{{}"));
console.log(validBraces("[]"));
console.log(validBraces("()))((()()(("));
console.log(validBraces("[({})]"))
