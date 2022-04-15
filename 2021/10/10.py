with open('input.txt' , 'r') as f : 
    
    syntax_map_values = {'(' : 3 , '{' : 1197 , '[' : 57 , '<': 25137}
    auto_completion_values = {'(' : 1 , '{' : 3, '[' : 2, '<': 4}
    back_map = {')' : '(' , '}' : '{' , '>' : '<' , ']' : '['}
    
    syntax_errors = []
    incomplete_lines = [] 
    for line in f : 
        
        ls = [] 
        for char in line : 
            if char == '\n' : 
                 temp = 0
                 for x in ls[::-1] : 
                    temp = temp * 5 + auto_completion_values[ls.pop()]
                 incomplete_lines.append(temp) 
                 continue 
            if char in back_map.values() : 
                 ls.append(char) 

            else : 
                 if back_map[char] == ls[-1] : 
                     ls.pop() 
                 else : 
                     syntax_errors.append(back_map[char]) 
                     break 

    incomplete_lines.sort()
    print(sum(map(lambda x : syntax_map_values[x] , syntax_errors)))
    print(incomplete_lines[len(incomplete_lines) // 2])
