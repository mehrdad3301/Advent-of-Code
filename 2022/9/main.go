package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {

	// pass 2 instead of 10 for first part 
	head := GetRope(10)
	seen := make(map[Knot]struct{})
	for move := range reader("in") {
		for i := 0; i < move.N; i++ {
			head.Move(move.Dir)
			knot := head
			for knot.PrevKnot != nil {
				knot = knot.PrevKnot
				knot.Follow(knot.NextKnot)
			}
			seen[*knot] = struct{}{}
		}
	}
	fmt.Println(len(seen))
}

func reader(fileName string) <-chan *Move {

	file, _ := os.Open(fileName)
	scn := bufio.NewScanner(file)

	moveStream := make(chan *Move)
	go func() {
		defer close(moveStream)
		for scn.Scan() {
			s := strings.Fields(scn.Text())
			n, _ := strconv.Atoi(s[1])
			dir := []rune(s[0])[0]

			moveStream <- &Move{Dir: dir, N: n}
		}
	}()
	return moveStream
}
