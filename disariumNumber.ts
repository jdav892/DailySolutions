export function disariumNumber(n: number){
    let newNum: string = String(n);
    let result: number = 0;
    for(let i = 0; i < newNum.length; i++){
        let exp: number = i + 1;
        result += Number(newNum[i]) ** exp;
    }
    return result === n ? "Disarium !!" : "Not !!"
}

//return String(n).split("").reduce((sum, x, i) => sum + parseInt(x) ** (i + ), 0) === n ? "Disarium !!" : "Not !!"