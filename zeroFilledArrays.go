func zeroFilledArrays(nums []int) int64 {
	var streak int64 = 0
	var total int64 = 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			streak++
			total += streak
		} else {
			streak = 0
		}
	}
	return total
}