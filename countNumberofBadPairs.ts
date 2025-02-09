function countBadPairs(nums: number[]): number {
    let good: number = 0
    let total: number = nums.length;
    let count: Record<number, number> = {}

    for(let i = 0; i < nums.length; i++){
        let key = nums[i] - i
        if(!(key in count)){
            count[key] = 0
        }
        good += count[key]
        count[key] = 1;
    }
    return total * (total - 1)/2 - good;
}