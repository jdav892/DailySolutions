package main

import (
	"fmt"
)

type NBAPlayer struct {
	Team string
	Ppg  float64
}

func sumPpg(playerOne, playerTwo NBAPlayer) float64 {
	/* total := playerOne.Ppg+playerTwo.Ppg
	return total */
	return playerOne.Ppg - playerTwo.Ppg
}

func main() {
	lbj := NBAPlayer{Team: "Lakers", Ppg: 27.0}
	mj := NBAPlayer{Team: "Bulls", Ppg: 30.1}

	fmt.Println(sumPpg(lbj, mj))
}
