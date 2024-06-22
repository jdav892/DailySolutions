function expandedForm(num){
    let numStr = num.toString();
    let expandedForm = [];

    for(let i = 0; i < numStr.length; i++){
        let digit = parseInt(numStr[i]);
        let place = Math.Pow(10, numStr.length - i - 1);

        if(digit !== 0){
            expandedForm.push(digit * place);
        }
    }
    return expandedForm.join(' + ')
}

// function expandedForm(num) {
//     return num.toString()
//         .split('')
//         .map((digit, index, arr) => digit * Math.pow(10, arr.length - index - 1))
//         .filter(expandedNum => expandedNum !== 0)
//         .join(' + ');
// }