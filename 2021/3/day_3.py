with open('input.txt' , 'r') as reader : 

    ls = [line.rstrip() for line in reader] 
index = 0    
s = len(ls[0]) 

while(len(ls) != 1) :  

    size = ones = 0 
    for line in ls : 
            size += 1 
            if(line[index] == '1'):
                ones += 1 
    
    temp = 0 
    if(ones < size/2):
        temp = 1 
    
    ls2 = list()
    for line in ls : 
        if(line[index] == str(temp)): 
            ls2.append(line) 
    
    ls = ls2 
    index += 1
    print(ls) 
print(int(ls2[0] , 2))       
