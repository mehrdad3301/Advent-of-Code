import re 

def checksub(x, y) : 
	return (x[0] >= y[0]) and (x[1] <= y[1])  

def subset(x , y) : 
	return checksub(y, x) or checksub(x, y)

def checklap(x, y) : 
	return (x[0] <= y[0] <= x[1]) or \
		   (y[0] <= x[0] <= y[1]) 

def overlap(x, y) : 
	return checklap(x, y) or checklap(y, x)	

with open('in', 'r') as f :
	data = [re.split('[-,]', line) for line in f.read().splitlines()]
	data = [list(map(int, d)) for d in data]

print(sum(subset(i[:2], i[2:]) for i in data)) 
print(sum(overlap(i[:2], i[2:]) for i in data)) 
