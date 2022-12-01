import numpy as np 
with open('input.txt' , 'r') as reader : 
    grid = np.zeros((1000, 1000) , int ) 

    for line in reader : 

            temp = [int(j) for i in line.rstrip().split('->') for j in i.strip().split(',')] 
            if temp[0] == temp[2] : 
                for j in range( min(temp[1] , temp[3]) ,  max(temp[1] , temp[3]) + 1) :
                    grid[j][temp[0]] += 1 

            elif temp[0] == temp[3] : 
                for i in range( min(temp[0] , temp[2]) ,  max(temp[0] , temp[2]) + 1) :
                    grid[temp[1]][i] += 1 
            else : 
                ls_1 = [i for i in range( min(temp[0] , temp[2]) ,  max(temp[0] , temp[2]) + 1)]
                ls_2 = [j for j in range ( min(temp[1] , temp[3]) ,  max(temp[1] , temp[3]) + 1)]
                if temp[1] > temp[3] : 
                    ls_2 = ls_2[::-1] 
                if temp[0] > temp[2] : 
                    ls_1 = ls_1[::-1]

                tup = list(zip(ls_1 , ls_2))
                for i , j in tup : 
                        grid[j][i] += 1 
        
            
    count = 0 
    for i in range(1000) : 
            for j in range(1000) : 
                if grid[i][j] >= 2 : 
                    count += 1 
                    
    print(count) 

