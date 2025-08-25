function longestSubarray(nums: number[]): number {
    let zero = 0
    let left = 0
    let best = 0

    for(let i = 0; i < nums.length; i++){
        if(nums[i] === 0){
            zero += 1
        }

        while(zero > 1){
            if(nums[left] === 0){
                zero -= 1
            }
            left += 1
        }
        best = Math.max(best, i - left + 1 - 1)
    }
    return best
}