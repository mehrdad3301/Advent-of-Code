
from itertools import product 
def get_adjacent(i , j) : 
	for dx , dy in ((1 , 0) , (-1 , 0) , (0 , 1) , (0 , -1) , (1 , 1) \
					, (1 , -1) , (-1 , 1) , (-1 , -1)) : 
		i1 , j1 = i + dx , j + dy 
		if 0 <= i1 < height and 0 <= j1 < width :
			yield i1 , j1 


	
def flash (i , j) : 
	global total 
	total += 1 
	flashed[i][j] = True
	for i1 , j1 in get_adjacent(i , j) : 
	
		if data[i1][j1] == 9 : 
			data[i1][j1] = 0 
			flash(i1 , j1) 
		
		elif data[i1][j1] != 0 : 
			data[i1][j1] = (data[i1][j1] + 1) % 10 
		
		else : 
			pass
		

with open('test' , 'r') as f : 
	data = [[int(x) for x in line]for line in f.read().splitlines()] 

width = len(data[0]) 
height = len(data)	
total , cnt = 0 , 0 
while True :
	cnt += 1  
	flashed = [[True if data[i][j] == 0 else False for j in range(width)] for i in range(height)]
	for i , j in product(range(height) , range(width)) : 
		data[i][j] = (data[i][j] + 1) % 10 

	for i , j in product(range(height) , range(width)) : 
		if  data[i][j] == 0 and not flashed[i][j] : 
				flash(i , j) 

	if all ( flashed[i][j] for i , j in product(range(height) , range(width)) ) : 
		print (cnt) 
		break

print(total) 
