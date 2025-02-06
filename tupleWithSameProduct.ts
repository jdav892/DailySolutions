function tupleSameProduct(nums: number[]): number {
    const uniques = Array.from(new Set(nums));
    const n = uniques.length;
    let count = 0;
    const counter = new Map<number, number>();

    for(let i = 0; i < n; i++){
        for(let j = i + 1; j < n; j++){
            const mult = uniques[i] * uniques[j]
            if (counter.has(mult)) {
                count += counter.get(mult)!;
                counter.set(mult, counter.get(mult)! + 1);
            }else {
                counter.set(mult, 1);
            }
        }
    }
    return count * 8;

};