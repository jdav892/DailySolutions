package kata

func Solve(s string) int {
	n := len(s)

	for l := n / 2; l > 0; l-- {
		if s[:l] == s[n-l:] {
			return l
		}
	}
	return 0
}
