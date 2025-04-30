/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
    let count = 0
    for(let i = 0; i < nums.length; i++){
        let val = nums[i].toString()
        if(val.length % 2 === 0){
            count++
        }
    }
    return count
};