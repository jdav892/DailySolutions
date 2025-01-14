export function pyramid(balls: number): number {
    let levels: number = 0;
    let total: number = 0;

    while(total + (levels + 1) <= balls){
        levels++;
        total += levels;
    }
    return levels;
}