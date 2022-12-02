movescore = { 'X':1 , 'Y':2 , 'Z':3 }

rules = { 'A': ['Y', 'X', 'Z'],
		  'B': ['Z', 'Y', 'X'], 
		  'C': ['X', 'Z', 'Y'] }

result = { 0: 6, 1: 3, 2: 0 }
win, draw, loss  = 0, 1, 2


def solve(game) : 

	opmove, urmove = game[0], game[1]
	return movescore[urmove] + outcome(opmove, urmove)

def outcome(opmove, urmove) :
	
	index = rules[opmove].index(urmove)			
	return result[index]	

def choose_move(game) : 
	opmove, urmove = game[0], game[1] 
	if urmove == 'X' :
		return rules[opmove][loss]
	elif urmove == 'Y' :
		return rules[opmove][draw]
	else :
		return rules[opmove][win]




with open('in' , 'r') as f : 

	games = [moves for moves in f.read().split("\n")]
	games = list(map(str.split, games))[:-1]


s2, s1 = 0, 0
for g in games : 
	s1 += solve(g)
	s2 += solve([g[0], choose_move(g)])

print(s1, s2)
