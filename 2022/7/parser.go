package main

import "strconv"

type Cd struct {
	TargetName string
}

type Ls struct {
	Nodes []Node
}

func parser(
	token <-chan string,
) <-chan interface{} {

	commands := make(chan interface{})

	parseLs := func() *Ls {

		l := &Ls{Nodes: make([]Node, 0)}
		for t, ok := <-token; t != "$" && ok; t, ok = <-token {

			if t == "dir" {

				name := <-token
				l.Nodes = append(l.Nodes, &Dir{Name: name})

			} else {

				size, _ := strconv.Atoi(t)
				name := <-token
				l.Nodes = append(l.Nodes, &File{Size: size, Name: name})

			}
		}
		return l
	}

	go func() {

		defer close(commands)

		for t, ok := <-token; ok; t, ok = <-token {

			if t == "$" {

				continue

			} else if t == "cd" {

				d := <-token
				commands <- &Cd{TargetName: d}

			} else if t == "ls" {
				commands <- parseLs()
			}

		}
	}()

	return commands
}
