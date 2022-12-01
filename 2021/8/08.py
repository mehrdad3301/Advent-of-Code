def foo(x , y) :
    for i in x : 
        if i in y : 
            pass 
        else :
            return False 
    return True 

with open('input.txt' , 'r+') as f : 
    sum = 0
    for line in f : 
        data = line.split('|')[0].strip().split(' ')
        value = line.split('|')[1].strip().split(' ')

        mapping = dict()
        
        for x in data : 
            if len(x) in [2 , 3 , 4 , 7] : 
                if len(x) == 2 : 
                    mapping[1] = x 
                elif len(x) == 3 : 
                    mapping[7] = x 
                elif len(x) == 4 : 
                    mapping[4] = x 
                else :
                    mapping[8] = x 
        
        sixer = [x for x in data if len(x) == 6]

        for x in sixer :   
            if foo(mapping[1] , x) :  
                pass 
            else : 
                mapping[6] = x 

        sixer.remove(mapping[6])
        for x in sixer : 
            if foo(mapping[4] , x) : 
                mapping[9] = x 
            else : 
                mapping[0] = x 

        fivers = [x for x in data if len(x) == 5]
        for x in fivers : 
            if foo(mapping[7] , x): 
                mapping[3] = x 
            elif foo(x ,mapping[9]) :  
                mapping[5] = x
            else :
                mapping[2] = x 

        ans = "" 
        for val in value : 
            for k , v in mapping.items() : 
                if sorted(v) == sorted(val) : 
                    ans += str(k) 
        
        sum += int(ans) 

    print(sum)