import heapq 
from math import inf

def get_adjacent(grid , i , j) : 
		
	for dx , dy in ((0 , 1) , (0 , -1) , (1 , 0) , (-1 , 0)) : 
		i1 , j1  = dx + i , dy + j 
		if 0 <= i1 < len(grid) and 0 <= j1 < len(grid[0]) : 
			yield i1 , j1	

def search( grid , width , height) : 

	dist = [[inf for _ in range(width)] for _ in range(height)]
	dist[0][0] = 0 
	heap = [(dist[0][0] , (0 , 0))] 
	visited = {(0, 0)} 
	
	while heap : 

		d , (i , j) = heapq.heappop(heap) 
		if i == height - 1 and j == width - 1 : 
			return d 		

		for i1 , j1 in get_adjacent(grid , i , j) : 

			if dist[i1][j1] > d + grid[i1][j1] and (i1 , j1) not in visited : 
				dist[i1][j1] = d + grid[i1][j1] 
				heapq.heappush(heap , (dist[i1][j1] , (i1 , j1)))

		visited |= {(i ,j)}


with open('input.txt' , 'r') as f : 
			
		data = [[int(x) for x in line] for line in f.read().splitlines()]

width = len(data[0])
height = len(data) 

new_data = [line * 5 for line in data * 5]
for i in range(height * 5) : 
	for j in range(width * 5) : 
		new_data[i][j] = (new_data[i][j] + i // height + j // width - 1) % 9 + 1  

print(search(data , width , height))		
print(search(new_data, width * 5 , height * 5 ) )	
	
