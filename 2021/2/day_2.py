depth = aim = pos = 0 
with open('input.txt' , 'r') as reader :
    lines = [line.rstrip() for line in reader] 
    for cmd in lines :
        temp = cmd.split()
        print(temp[0]) 
        print(temp[1]) 
        x = int(temp[1]) 
        if( temp[0] == 'forward') : 
            pos += x
            depth += aim*x
        elif( temp[0] == 'down') : 
            aim += x  
        else : 
            aim -= x

print(pos*depth) 
