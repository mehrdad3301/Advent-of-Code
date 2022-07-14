import re 
def is_valid(x , y , data) : 
	return [(data[2] + 1) / y] >= [x - (2*-y + 1)] >= [(data[3] + 1) / y] 
	
def solve() : 
	mx = 0 
	for x in range(0 , data[1] + 1) : 
		for y in range(0 , -data[2]) : 
			if is_valid(x , y) and y > mx : 
				mx = y 
	return mx 


def read(address) : 
	with open(address) as f : 
		return list(map(lambda x : int(x) ,re.findall(r'[0-9]+' , f.read()))) 
		 
data = read('17.in') 

print(solve()) 
