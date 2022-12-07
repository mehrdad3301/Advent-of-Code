package main

import "fmt"

type Node interface {
	Type() string
}

type Dir struct {
	Name     string
	Parent   *Dir
	Children []*Dir
	Files    []*File
	Size     int
}

func (d *Dir) Type() string { return "DIR" }

type File struct {
	Name string
	Size int
}

func (f *File) Type() string { return "FILE" }

var (
	memSize   = 70000000
	neededMem = 30000000
)

func main() {

	root := &Dir{Name: "/"}
	currDir := root

	for c := range parser(lexer("in")) {
		if cd, ok := c.(*Cd); ok {
			currDir = currDir.moveDir(cd.TargetName)
		} else if ls, ok := c.(*Ls); ok {
			currDir.listDir(ls)
		}
	}
	findSize(root)
	fmt.Println(dfs1(root))
	fmt.Println(dfs2(root, neededMem-(memSize-root.Size)))
	//tree(root, "")
}

func dfs1(d *Dir) int {

	var sum int
	for _, c := range d.Children {
		sum += dfs1(c)
	}
	if d.Size < 100000 {
		return d.Size + sum
	}
	return sum
}

func dfs2(d *Dir, neededFreed int) int {

	min := memSize
	if d.Size < neededFreed {
		return min
	}
	for _, c := range d.Children {
		s := dfs2(c, neededFreed)
		if s < min {
			min = s
		}
	}
	if min == memSize {
		return d.Size
	}
	return min
}

func (currDir *Dir) moveDir(target string) *Dir {

	if target == ".." {
		return currDir.Parent
	} else if target == "/" {
		dir := currDir
		for dir.Parent != nil {
			dir = dir.Parent
		}
		return dir
	}
	for _, dir := range currDir.Children {
		if target == dir.Name {
			return dir
		}
	}
	return currDir
}

func (currDir *Dir) listDir(ls *Ls) {

	for _, node := range ls.Nodes {

		if node.Type() == "DIR" {

			node := node.(*Dir)
			node.Parent = currDir
			currDir.Children = append(currDir.Children, node)

		} else if node.Type() == "FILE" {

			node := node.(*File)
			currDir.Files = append(currDir.Files, node)

		}
	}
}

func findSize(d *Dir) int {

	var size int
	for _, f := range d.Files {
		size += f.Size
	}

	for _, c := range d.Children {
		size += findSize(c)
	}
	d.Size = size
	return size
}

func tree(d *Dir, tab string) {

	fmt.Println(tab+d.Name, d.Size)
	for _, f := range d.Files {
		fmt.Println(tab+"  "+f.Name, f.Size)
	}

	for _, c := range d.Children {
		tree(c, tab+"  ")
	}
}
