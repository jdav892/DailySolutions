export function arr2bin(arr: any[]): string {
    const binSum = arr.reduce((acc, curr) => acc + (typeof curr === "number" ? curr : 0 ), 0);
    return binSum.toString(2); 
}