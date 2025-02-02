function isArraySpecial(nums: number[]): boolean {
    for(let i = 1; i < nums.length; i++){
        if((nums[i] & 1) === (nums[i - 1] & 1)){
            return false
        }
    }
    return true
}