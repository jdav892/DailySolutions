export function oddOnesOut(nums: number[]) { 
    const map: Record<number, number> = {};

    nums.filter((value: number): void => {
        if(!map[value]) {
            map[value] = 0
        }
        map[value] += 1
    })
    let final: number[] = nums.filter((num: number): boolean => map[num] % 2 === 0);
    return final
}