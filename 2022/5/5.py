from itertools import zip_longest
import re

def move(m, c, k) : 

	num, src, dst = m
	c[dst - 1] += c[src - 1][-num:][::k]
	del c[src - 1][-num:]

with open('in', 'r') as f : 
	
	crates, moves = f.read().split("\n\n")
	
	crates = crates.splitlines()[:-1]
	crates = [c[1::4] for c in crates]
	crates = [*zip_longest(*crates[::-1], fillvalue=" ")]
	crates = [ [ l for l in c if not str.isspace(l)] for c in crates ]

	moves = re.findall(r'move (\d+) from (\d+) to (\d+)', moves) 
	moves = [list(map(int, m)) for m in moves]

c_9000 = [c[:] for c in crates] 
for m in moves : 
	move(m, c_9000, -1)
	
c_9001 = [c[:] for c in crates] 
for m in moves : 
	move(m, c_9001, 1)
		
print("".join([x[-1] for x in c_9000]))
print("".join([x[-1] for x in c_9001]))
	
