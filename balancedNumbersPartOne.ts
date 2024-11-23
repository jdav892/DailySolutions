export function balancedNum(number: number): string{
    let numStr: string = String(number);
    let result: number = 0;
    for(let i = 0; i < numStr.length/2 - 1; i++){
        result += Number(numStr[i]) - Number(numStr[numStr.length - 1 - i])
    }
    return result === 0 ? "Balanced" : "Not Balanced"
}