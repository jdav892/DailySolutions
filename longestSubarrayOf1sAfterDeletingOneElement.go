func longestSubarray(nums []int) int {
	zero := 0
	left := 0
	best := 0

	for i := 0; i < nums.length; i++ {
		if nums[i] == 0 {
			zero += 1
		}

		for zero > 1 {
			if nums[left] == 0 {
				zero -= 1
			}
			left += 1
		}
		best = max(best, i-left+1-1)
	}
	return best
}