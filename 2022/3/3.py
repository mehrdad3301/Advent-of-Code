
def priority(s) : 	
	if s.islower() : 
		return ord(s) - ord('a') + 1 
	else :
		return ord(s) - ord('A') + 27 

def shared(*args) : 
	s = set.intersection(*[set(a) for a in args]).pop()
	return priority(s)

with open('in', 'r') as f : 
	items = [item.strip() for item in f.readlines()] 

print(sum([shared(i[:len(i)//2], i[len(i)//2:]) for i in items]))
print(sum([shared(*items[i: i+3]) for i in range(0, len(items), 3)]))


