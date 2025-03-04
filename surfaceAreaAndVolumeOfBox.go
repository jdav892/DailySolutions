package kata

func GetSize(w, h, d int) [2]int {
	area := 2 * ((w * h) + (w * d) + (h * d))
	volume := w * h * d
	totalSurfaceArea := [2]int{area, volume}
	return totalSurfaceArea
}
