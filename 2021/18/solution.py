import re 
REMOVE_OUTER_BRACKETS = re.compile(r'\[(.*)\]')
GET_PAIRS = re.compile(r'(\[?.*\]?),(\[?.*\]?)') 

class Tree :

	def __init__(self , s:str) : 
		print(s)
		if len(s) != 1 : 
			self._value = parser(s) 
			self._left = Tree(self._value[0])
			self._right = Tree(self._value[1]) 	
		return self 

	def __str__(self) : 
		return "[" + \
				str(self._left) + "," + str(self._right) + \
			   "]"

def parser(s:str) -> (str , str) : 

	if len(s) == 1 :
		return s  

	x = REMOVE_OUTER_BRACKETS.findall(s)  
	try : 
			_left_child = GET_PAIRS.match(*x).group(1) 
			_right_child = GET_PAIRS.match(*x).group(2)
			return _left_child , _right_child
	except TypeError : 
		print('error' , x) 

s = '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]' 
print(Tree(s))
