
class Lanter_Fish : 
    child_cycle = 8 
    adult_cycle = 6 
    def __init__(self , remaining_days = None, is_child = False) : 
        self.is_child = is_child 
        if is_child : 
            self.remaining_days = Lanter_Fish.child_cycle  
        else : 
            self.remaining_days = remaining_days         
    def __neg__(self) : 
       if self.remaining_days == 0 :  
            self.is_child = False 
            self.remaining_days = Lanter_Fish.adult_cycle  
            return Lanter_Fish.reproduce()
       else : 
           self.remaining_days -= 1 
    def reproduce() : 
        return Lanter_Fish(is_child = True)
    def __str__(self) : 
        return f'{self.remaining_days} '
    def __repr__(self) : 
        return f'{self.remaining_days} '
#with open('input.txt' , 'r') as reader : 
#    ls = [Lanter_Fish(int(i)) for i in reader.readline().split(',')]
#
#    for i in range (80) : 
#
#        temp = list() 
#        for fish in ls : 
#            x = -fish 
#            if x : 
#                temp.append(x) 
#        if temp : 
#            ls = ls + temp 
#        
#        print(f"day{i+1} : {len(ls)}")     
ls = [300 , 509, 538, 557, 578, 600 , 600 ,600 , 809]
for i in range(256) : 
    ls.append(ls[i]+ ls[i + 2])
    print(f"day{i+10} {ls[-1]}")
print(ls)
