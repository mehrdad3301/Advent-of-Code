def read_file() : 
	with open('13.in') as f : 
		points , folds = f.read().split('\n\n')	
		points = points.strip().split('\n') 
		points = [list(map(int , line.split(','))) for line in points]
		folds = folds.strip().split('\n') 
		folds = [line.split('=') for line in folds]	
		return points , folds 

def load_grid(points) : 
	width = max(x for x , y in points) 
	height = max(y for x , y in points) 
	grid = [[0 for _ in range(width + 1)] for _ in range(height + 1)] 
	for x , y in points : 
		grid[y][x] = 1 
	return grid 


def fold(grid , axis , line) : 
	global width , height 
	if axis == 'x' : 
		for x in range(line , width) :
			for y in range(height) : 
				if grid[y][x]: 
					grid[y][x - 2 * (x - line)] = 1 
		width = line 
	else : 
		for x in range(width) : 
			for y in range(line , height) : 
				if grid[y][x] : 
					grid[y - 2 * (y - line)][x] = 1 
		height = line 


def print_grid(grid) : 
	for y in range(height) : 
		for x in range(width) : 
			print(grid[y][x] , end = '') 
		print() 

	print() 


points , folds = read_file() 
grid = load_grid(points) 
width , height = len(grid[0]) , len(grid) 

for axis , line in folds : 
	fold(grid , axis , int(line)) 
	print(sum(grid[y][x] for y in range(height) for x in range(width))) 
print_grid(grid) 
