with open('input.txt' , 'r') as f , open('in.txt' , 'w') as x : 
    data = ""
    for line in f : 
       if '|' in line : 
           line = line.replace('\n' , ' ')
       data = data + line 

    
    x.write(data)