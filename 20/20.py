from itertools import product
def reader() : 

	with open('20.in') as f : 
		algorithm , image = f.read().split('\n\n') 
	algorithm = ''.join(algorithm.split('\n')) #for Vim users only :) 
	image = image.split('\n')
	image.pop() 
	return algorithm , image 

algorithm , image = reader() 

def get_binary(s) : 
	return int(s.translate(s.maketrans({'#' : '1' , '.' : '0'})) , 2) 

def get_surrounding(image , x , y , pad_val) : 
	
	height , width = len(image) , len(image[0]) 
	s = [pad_val if i < 0 or j < 0 or i >= height or j >= width else image[i][j] \
		for i , j in product(range(x - 1 , x + 2) , range(y - 1 , y + 2))] 

	return ''.join(s)  

def add_padding(image , pad_val='.') :

	sides = pad_val 
	tops = (pad_val * (len(image[0]) + 2)) 
	img =   [tops , 
			*[sides + line + sides for line in image] , 
			tops] 
	return img 
	
def enhance_image(image , pad_val='.') : 
		
	image = add_padding(image, pad_val)  
	height , width = len(image) , len(image[0]) 
	enhanced_image  = image.copy()  
	for i in range(height): 
		enhanced_image[i] = ''.join([algorithm[get_binary(get_surrounding(image , i ,j, pad_val))]\
								    for j in range(width)]) 
	
	return enhanced_image 


for x in range(50) : 
	image = enhance_image(image , '.' if x % 2 == 0  else '#') 	
	if x == 1 : 
		print(sum(1 if x == '#' else 0 for line in image for x in line))
print(sum(1 if x == '#' else 0 for line in image for x in line))
