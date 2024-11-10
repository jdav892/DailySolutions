/**
 * @param {number[]} nums
 * @param {number} maximumBit
 * @return {number[]}
 */
var getMaximumXor = function(nums, maximumBit) {
    let x = 0
    for(n in nums){
        x ^= n
    }

    let sub = (1 << maximumBit) - 1
    let answer = []
    for(n in nums){
        answer.push(x ^ sub)
        x ^= n
    }
    return answer
}