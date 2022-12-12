package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {

	i := 1
	sum := 0
	var CRT strings.Builder
	for x := range cpu(reader("in")) {
		CRT.WriteRune(getCurrPixel(x, (i-1) % 40)
		if i%40 == 20 {
			sum += x * i
		}
		if i%40 == 0 {
			CRT.WriteRune('\n')
		}
		i += 1
	}
	fmt.Println(sum)
	fmt.Println(CRT.String())

}

func getCurrPixel(x, i int) rune {

	fmt.Println("x, i", x, i)
	if abs(x-i) <= 1 {
		return '#'
	}
	return '.'
}

func cpu(instructions <-chan string) <-chan int {

	x := 1
	register := make(chan int)

	go func() {
		defer close(register)

		for instr := range instructions {
			if instr == "noop" {
				register <- x
			} else {
				num := strings.Fields(instr)[1]
				addNum, _ := strconv.Atoi(num)
				register <- x
				register <- x
				x += addNum
			}
		}

	}()

	return register
}
func reader(fileName string) <-chan string {

	file, _ := os.Open(fileName)
	scn := bufio.NewScanner(file)

	instructions := make(chan string)

	go func() {
		defer close(instructions)
		for scn.Scan() {
			instructions <- scn.Text()
		}
	}()

	return instructions

}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}