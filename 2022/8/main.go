package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {

	grid := getGrid("in")
	h, w := len(grid), len(grid[0])

	var visible, maxScene int
	for i, r := range grid {
		if i == 0 || i == h-1 {
			continue
		}

		for j, _ := range r {
			if j == 0 || j == w-1 {
				continue
			}

			b1, v1 := checkUp(grid, i, j)
			b2, v2 := checkRight(grid, i, j)
			b3, v3 := checkLeft(grid, i, j)
			b4, v4 := checkDown(grid, i, j)

			if !(b1 && b2 && b3 && b4) {
				visible++
			}
			scenicScore := v1 * v2 * v3 * v4
			if scenicScore > maxScene {
				maxScene = scenicScore
			}

		}
	}
	fmt.Println(visible + 2*h + 2*w - 4)
	fmt.Println(maxScene)
}

func getGrid(fileName string) [][]int {

	input, _ := os.Open(fileName)
	scn := bufio.NewScanner(input)
	grid := make([][]int, 0)

	for i := 0; scn.Scan(); i++ {
		grid = append(grid, []int{})
		for _, s := range scn.Text() {
			grid[i] = append(grid[i], int(s-'0'))
		}
	}

	return grid
}

func checkUp(grid [][]int, i, j int) (bool, int) {

	for k := i - 1; k >= 0; k-- {
		if grid[k][j] >= grid[i][j] {
			return true, i - k
		}
	}
	return false, i

}

func checkDown(grid [][]int, i, j int) (bool, int) {
	h := len(grid)
	for k := i + 1; k < h; k++ {
		if grid[k][j] >= grid[i][j] {
			return true, k - i
		}
	}
	return false, h - i - 1
}

func checkRight(grid [][]int, i, j int) (bool, int) {
	w := len(grid[0])
	for k := j + 1; k < w; k++ {
		if grid[i][k] >= grid[i][j] {
			return true, k - j
		}
	}
	return false, w - j - 1
}
func checkLeft(grid [][]int, i, j int) (bool, int) {

	for k := j - 1; k >= 0; k-- {
		if grid[i][k] >= grid[i][j] {
			return true, j - k
		}
	}
	return false, j
}
