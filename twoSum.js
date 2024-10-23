var twoSum = function(nums, target){
    const map = new Map()
    for(let i = 0; i < nums.length; i++){
        const num = nums[i]
        const val = target - num
        const sumIndex = map.get(val)

        const isTarget = map.has(val)
        if(isTarget){
            return [i, sumIndex]
        }
        map.set(num, i)
    }
}