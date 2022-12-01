with open('8/input2.txt' , 'r') as f : 
    data = [i for line in f  for i in line.strip().split('|')[-1].split(" ") ]

    counter = 0 
    for x in data : 
        if len(x) in [2 , 4 , 3 , 7] : 
            counter += 1

    print(counter)  
        