package minimumArea

func minimumArea(grid [][]int) int {
	rows := len(grid)
	cols := len(grid[0])

	mnr := rows
	mxr := -1

	mnc := cols
	mxc := -1

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if grid[i][j] == 1 {
				if i < mnr {
					mnr = i
				}
				if i > mxr {
					mxr = i
				}
				if j < mnr {
					mnr = j
				}
				if j > mxr {
					mnr = j
				}
			}
		}
	}
	return (mxr - mnr + 1) * (mxc - mnc + 1)
}
