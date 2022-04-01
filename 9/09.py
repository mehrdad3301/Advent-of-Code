from bisect import insort 
from itertools import product 
from collections import deque
from math import prod 

def get_adjacent(data , i , j) : 
	
	for dx , dy in ((0 , 1) , (0 , -1) , (1 , 0) , (-1 , 0)) : 
		i1 , j1 = dx + i , dy + j 
		if 0 <= i1 < len(data) and 0 <= j1 < len(data[0]) : 
			yield i1 , j1 

def bfs(data ,i , j) : 
	queue = deque([(i , j)])	
	marked = {(i , j)} 
	while queue : 

		x , y = queue.popleft()	
		for i1 , j1 in get_adjacent(data , x , y) : 
			if (i1 , j1) not in marked and data[i1][j1] != 9 : 
				queue.append((i1 , j1)) 
		
		marked.add((x , y))
		
	return len(marked) 	

with open('input.txt' , 'r') as f : 

	data = [[int(i) for i in line]for line in f.read().splitlines()]

risks =  []	
basins = []
for i , j in product(range(len(data)) , range(len(data[0])) ) : 
	
	if all(data[i][j] < data[i1][j1]  for i1 , j1 in get_adjacent(data , i , j)):

		risks.append(data[i][j] + 1) 			
		insort(basins , bfs(data , i , j))

print(sum(risks))
print(prod(basins[-3:]))
