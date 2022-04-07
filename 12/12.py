def DFS(x , marked , repeat) : 

	if x == 'end' : 	
		return 1 
	
	paths = 0 
	for v in data[x] : 

		if v == 'start' : 
			continue 

		if not (v.islower() and v in marked) :
			paths += DFS(v , marked | {v} , repeat ) 
		elif repeat : 
			paths += DFS(v , marked , False) 

	return paths 

with open('in') as f : 
	data = {} 
	for line in f : 
		u , v = line.strip().split('-') 
		data[u] = [v] if u not in data else data[u] + [v]  
		data[v] = [u] if v not in data else data[v] + [u]  


print(DFS('start' , set() , False))
print(DFS('start' , set() , True)) 
