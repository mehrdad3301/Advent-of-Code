import re 

def exec_command(grid, data) : 
	for command in get_command(data) : 
		c , *v = command  
		x , y , z = v 
		for i in range(int(x[0]) , int(x[1]) + 1) : 
			for j in range(int(y[0]) , int(y[1]) + 1) : 
				for k in range(int(z[0]) , int(z[1]) + 1) : 
					for m in [i , j , k] : 
						if m < 0 : 
							m = 50 + m * -1 
					grid[i][j][k] = 1 if c == 'on' else 0 	
									
		print(sum(z for x in grid for y in x for z in y)) 
def get_command(data) : 
	for v in data : 
		yield v 
	
def read_file() : 
	with open('22.in') as f : 
		t = [(line.split()[0] , re.findall(r'-?\d{1,2}\.\.\-?\d{1,2}' , line)) for line in f.readlines()]
		return [(e[0] , *[x.split('..') for x in e[1]]) for e in t] 

data = read_file() 
grid = [[[0 for _ in range(100)]for _ in range(100)]for _ in range(100)]
exec_command(grid , data) 
print(sum(z for x in grid for y in x for z in y)) 
