export function maxIntChain(n: number): number {
    interface values {
        one: number;
        two: number;
    }
    
    if(n < 5){
        return -1
    }

    let one = Math.floor(n / 2) + 1
    let two = Math.floor(n / 2)
    if(n % 2 === 0){
        two -= 1
    }
    return one * two
}