package kata

import (
	"sort"
)

func WrapPresent(height, width, length int) int {
	p1 := 2 * (height + width)
	p2 := 2 * (length + width)
	p3 := 2 * (height + length)

	perimeter := []int{p1, p2, p3}
	sort.Ints(perimeter)
	return perimeter[0] + perimeter[1] + 20
}
