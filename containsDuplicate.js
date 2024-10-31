/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const numsMap = {};
    
    for(num of nums){
        if(numsMap[num]){
            return true; 
        }else{
            numsMap[num] = 1; 
        }
    }
    return false;

};

//const containsDupe = (nums) =>{
//  return new Set(nums).size !== nums.length; 
//}

//O(n)