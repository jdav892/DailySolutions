function solution(nums){
    if(nums === nul){
        return []
    }
    return nums.sort(function(a, b) {return a - b})
}