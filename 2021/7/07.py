with open('t.txt' , 'r') as f : 
    
    ls = [int(i) for i in f.readline().split(',')]

    distances = set() 
    for i in range(max(ls)) : 

        m = map(lambda x : abs(x - i) * (abs(x-i) + 1) // 2 , ls)
        distances.add(sum(m))

    print(min(distances)) 
