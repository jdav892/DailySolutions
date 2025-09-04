func findClosest(x int, y int, z int) int {
	xDiff := int(math.Abs(float64(z - x)))
	yDiff := int(math.Abs(float64(z - y)))

	if xDiff < yDiff {
		return 1
	} else if yDiff < xDiff {
		return 2
	} else {
		return 3
	}
}