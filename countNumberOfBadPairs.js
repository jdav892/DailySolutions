/**
 * @param {number[]} nums
 * @return {number}
 */
var countBadPairs = function(nums) {

    const n = nums.length
    let total = n * (n - 1) / 2;
    const diff = new Map();
    for(let i = 0; i < n; i++){
        const dif = nums[i] - i
        total -= diff.get(dif) || 0;
        diff.set(dif, (diff.get(dif) || 0) + 1);
    }
    return total;
}