export function height(n: number): string {
    const start: number = 2000000;
    let result: number = 0;

    for(let i = 0; i <= n; i++){
        result += start / 2.5 ** i;
    }
    return result.toFixed(3);
}