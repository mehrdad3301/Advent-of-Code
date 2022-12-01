import numpy as np 

class Board :

    class Element : 
    
        def __init__(self , value) :
            self.value = value 
            self.visited = False  
        def visit(self) : 
            visited = True 
        def __getitem__(self) : 
            return (value , visited) 
        def __str__(self) : 
            return f"{self.value} , {self.visited}" 

    def __init__(self , arr) : 
        self.size = len(arr[0]) 
        self.board = list(range(self.size)) 
        for i in range(self.size) : 
            self.board[i] = [self.Element(arr[i][j]) for j in range(self.size)]
        self.row = np.zeros(self.size)  
        self.column = np.zeros(self.size) 
    
    def check_value(self , x) : 
        for i in range(self.size) :
            for j in range(self.size) :
                if(self.board[i][j].value == x) :
                    self.board[i][j].visited = True 
                    self.row[i] += 1 
                    self.column[j] += 1 
                    
    def check_bingo(self , key) : 
        if self.size in self.row or self.size in self.column: 
            summ  = 0 

            for i in range(self.size) : 
                flag = False
                for j in range(self.size) : 
                    if self.board[i][j].visited == False :
                        summ += int(self.board[i][j].value)
                        flag = True 
            return summ * int(key) 
        
        else :  
            return False  

def read_line(reader , st = None) : 
    return reader.readline().rstrip().split(st) 

with open('input.txt' , 'r') as reader : 
    
    keys = read_line(reader , ',')  
    
    reader.readline() 
    line = read_line(reader) 
     
    temp = list()
    boards = list() 
    temp.append(line)  

    for l in reader :
        if(l == "\n" or l == ''):
            x = Board(temp)
            boards.append(x) 
            temp = list() 
            continue 
        temp.append(l.rstrip().split()) 
    boards.append(Board(temp))  
    
    
    for key in keys : 
        flag = False 

        for board in boards : 
            board.check_value(key) 
            x = board.check_bingo(key) 
            if x != False  : 
                print(x) 
                flag = True 
                break
        if flag :
            break
