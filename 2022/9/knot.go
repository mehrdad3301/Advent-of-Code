package main

type Move struct {
	Dir rune
	N   int
}

type Knot struct {
	x, y     int
	PrevKnot *Knot
	NextKnot *Knot
}

func (k *Knot) MoveRight() {
	k.x += 1
}
func (k *Knot) MoveLeft() {
	k.x -= 1
}
func (k *Knot) MoveUk() {
	k.y += 1
}
func (k *Knot) MoveDown() {
	k.y -= 1
}

func (k *Knot) Move(dir rune) {

	if dir == 'R' {
		k.MoveRight()
	} else if dir == 'L' {
		k.MoveLeft()
	} else if dir == 'U' {
		k.MoveUk()
	} else if dir == 'D' {
		k.MoveDown()
	}
}

func (k1 *Knot) Follow(k2 *Knot) {

	if k1.IsNeigbor(k2) {
		return
	} else if k1.x == k2.x {
		if k1.y > k2.y {
			k1.y -= 1
		} else {
			k1.y += 1
		}
	} else if k1.y == k2.y {
		if k1.x > k2.x {
			k1.x -= 1
		} else {
			k1.x += 1
		}
	} else {
		if k2.x > k1.x {
			k1.MoveRight()
		} else {
			k1.MoveLeft()
		}
		if k2.y > k1.y {
			k1.MoveUk()
		} else {
			k1.MoveDown()
		}
	}
}

func (k1 *Knot) IsNeigbor(k2 *Knot) bool {
	if abs(k1.x-k2.x) <= 1 &&
		abs(k1.y-k2.y) <= 1 {
		return true
	}
	return false
}

func GetRope(n int) *Knot {
	head := &Knot{x: 0, y: 0}
	h := head
	for i := 0; i < n-1; i++ {
		k := &Knot{x: 0, y: 0}
		h.PrevKnot = k
		k.NextKnot = h
		h = k
	}
	return head
}
func abs(x int) int {
	if x < 0 {
		x = -x
	}
	return x
}
