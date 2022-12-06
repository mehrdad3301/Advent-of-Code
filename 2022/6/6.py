

def solve(signal, p): 
	for i in range( len(signal) - p) : 
		if len( set(signal[i: i+p]) ) == p : 
			return i + p

with open('in', 'r') as f :
	signal = f.read().strip()

print(solve(signal, 4))
print(solve(signal, 14))
