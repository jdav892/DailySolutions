function validBraces(braces){
    const stack = []
    const braceMap = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    };
    for (let brace in braces){
        if (braceMap[brace]){
            stack.push(braceMap[brace])
        }else{
            if (stack.pop() !== brace){
                return false;
            }
        }
    }
    return stack.length === 0;
}