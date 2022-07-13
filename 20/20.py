import re 







def reader() : 

	with open('20.in') as f : 
		s = f.read() 	
	algorithm = re.split(r'\n\n' , s)[0] 
	image = [] 
	temp = re.split(r'\n\n' , s)[1]
	temp = re.split(r'\n' , temp)
	temp.pop() 
	for v in temp : 
		image.append(list(v)) 
	return algorithm , image 

algorithm , image = reader() 
