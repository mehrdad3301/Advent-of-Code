with open ('input.txt' , 'r') as reader : 

    data = [int(x , 2) for x in reader] 
    bits = max([x.bit_length() for x in data]) 

    gamma = 0 
    for i in range(bits) : 
        gamma_bit = sum((x >> i) & 1 for x in data ) > len(data) // 2  
        gamma |= gamma_bit << i 
    
    x = 2 ** bits 
    y = gamma  
    print(x , y , gamma ,bin(1) ,bin(gamma) ,   x - y) 
    print(gamma , ~gamma , ~bin(gamma)) 
