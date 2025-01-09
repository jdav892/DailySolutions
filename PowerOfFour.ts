export function powerOf4(n: any): boolean {
    if(typeof n !== "number" || n <= 0) return false

    return (n & (n - 1)) === 0 && (n - 1) % 3 === 0
}