counter = 0 
with open('input.txt' , 'r') as reader : 
    
    lines = [int(i) for i in reader.readlines() if i != '\n']
    
    for i in range(len(lines)-3) :
        if(lines[i] < lines[i+3]) :
            counter += 1
        print(lines[i+3]) 
print(counter) 
