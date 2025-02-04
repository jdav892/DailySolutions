function longestMonotonicSubarray(nums: number[]): number {
    let current: number = 1
    let result: number = 1
    let increase: number = 0
    
    for(let i = 1; i < nums.length; i++){
        if(nums[i - 1] < nums[i]){
            if(increase > 0){
                current++
            }else{
                current = 2
                increase = 1
            }
        }else if(nums[i - 1] > nums[i]){
            if(increase < 0){
                current++
            }else{
                current = 2
                increase = -1
            }
        }else{
            current = 1
            increase = 0
        }
        result = Math.max(current, result)
    }
    return result
}