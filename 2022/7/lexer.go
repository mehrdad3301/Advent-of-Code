package main

import (
	"bufio"
	"os"
	"strings"
)

func lexer(
	filename string,
) <-chan string {

	fileReader, _ := os.Open(filename)
	scn := bufio.NewScanner(fileReader)

	token := make(chan string)

	go func() {
		defer close(token)

		for scn.Scan() {

			for _, s := range strings.Fields(scn.Text()) {
				token <- s
			}
		}
	}()

	return token
}
