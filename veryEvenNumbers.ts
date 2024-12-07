export function isVeryEvenNumber(n: number): boolean {
    while(n >= 10){
        n = n
        .toString()
        .split("")
        .reduce((sum, digit) => sum + Number(digit), 0)
    }

    return n % 2 === 0;

}