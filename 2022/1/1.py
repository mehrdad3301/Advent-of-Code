
with open('in', 'r') as f : 
	input = f.read().split("\n\n") 
	data = list(map(str.split, input))

s = sorted([sum(map(int, v)) for v in data])
print(s[-1]) 
print(sum(s[-3:])) 
