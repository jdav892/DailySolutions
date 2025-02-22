export function maxIntChain(n: number): number {
    if(n < 5){
        return -1
    }

    let one: number = Math.floor(n / 2) + 1
    let two: number = Math.floor(n / 2)
    if(n % 2 === 0){
        two -= 1
    }
    return one * two
}