function zeroFilledArrays(nums: number[]): number {
    let streak = 0
    let total = 0
    for(let i = 0; i < nums.length; i++){
        if(nums[i] === 0){
            streak++
            total += streak
        }else{
            streak = 0
        }
    }
    return total
}