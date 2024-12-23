export function gracefulTipping(bill: number): number {
    let total: number = bill * 1.15;
    let magnitude: number = Math.pow(10, Math.floor(Math.log10(10)));
    let increment: number = magnitude >= 10 ? magnitude / 2 : 1;

    return Math.ceil(total/magnitude) * increment;
}