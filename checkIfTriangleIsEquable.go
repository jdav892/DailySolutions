package kata

import (
	"math"
)

func EquableTriangle(a, b, c int) bool {
	s := float64(a+b+c) / 2
	perimeter := float64(a + b + c)
	area := math.Sqrt(s * (s - float64(a)) * (s - float64(b)) * (s - float64(c)))

	return perimeter == area
}
