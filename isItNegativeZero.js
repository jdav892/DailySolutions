export function isNegativeZero(n:number):boolean {
    return Object.is(n, -0)
}