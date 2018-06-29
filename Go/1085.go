package main

import "fmt"

func main() {

	var a, b, c, d int

	fmt.Scanf("%d %d %d %d", &a, &b, &c, &d)

	out := a - 0

	if b-0 < out {
		out = b - 0
	}
	if d-b < out {
		out = d - b
	}
	if c-a < out {
		out = c - a
	}
	fmt.Print(out)
}
