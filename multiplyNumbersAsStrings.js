function multiply(a, b){
    const newNum1 = a.split("").reverse().map(Number);
    const newNum2 = b.split("").reverse().map(Number);

    let newArr = Array(newNum1.length + newNum2.length).fill(0);

    for(let i = 0; i < newNum2.length; i++){
        let over = 0;
        for(let j = 0; j < newNum1.length; j++){
            const result = newNum1[j] * newNum2[i] + over + newArr[i + j];
            over = Math.floor(result / 10);
            newArr[i + j] = result % 10;
        }
        newArr[i + newNum1.length] = over;
    }
    while(newArr.length > 1 && newArr[newArr.length - 1] === 0){
        newArr.pop()
    }
    const arrStr = newArr.reverse().join("");
    return arrStr

}