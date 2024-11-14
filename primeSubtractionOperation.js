/**
 * @param {number[]} nums
 * @return {boolean}
 */
var primeSubOperation = function(nums) {
    const primes = [];

    for(let i = 2; i <= 1000; i++){
        let isPrime = true;
        for(const prime of primes){
            if(i % prime === 0){
                isPrime = false;
                break;
            }
        }
        if(isPrime){
            primes.push(i)
        }   
    }

    const searchPrimeIndex = (x) => {
        let left = 0;
        let right = primes.length;
        while(left < right){
            const mid = (left + right) >> 1;
            if(primes[mid] > x){
                right = mid;
            }else{
                left = mid + 1
            }
        }
        return left;
    }
    
    const count = nums.length;
    for(let i = count - 2; i >= 0; i--){
        if(nums[i] < nums[i + 1]){
            continue;
        }
        const primeIndex = searchPrimeIndex(nums[i] - nums[i + 1]);
        if(primeIndex === primes.length || primes[primeIndex] >= nums[i]){
            return false;
        }
        nums[i] -= primes[primeIndex];
    }
    return true;
};