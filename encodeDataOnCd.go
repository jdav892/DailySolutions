package kata

func EncodeCd(n uint8) string {
	result := []rune{'P'}

	for i := 0; i < 8; i++ {
		bit := (n >> i) & 1
		if bit == 1 {
			if result[len(result)-1] == 'P' {
				result = append(result, 'L')
			} else {
				result = append(result, 'P')
			}
		} else {
			result = append(result, result[len(result)-1])
		}
	}
	return string(result)
}
