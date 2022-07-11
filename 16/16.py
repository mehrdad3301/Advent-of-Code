import math
import operator
from dataclasses import dataclass

OPS = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    4: next,
    5: lambda x: operator.gt(*x),
    6: lambda x: operator.lt(*x),
    7: lambda x: operator.eq(*x),
}

@dataclass 
class Bits : 
	data : int 
	num_bits : int 
	
	
	def get(self , n) : 
		self.num_bits -= n 
		vl = self.data >> self.num_bits 
		self.data &= 2 ** self.num_bits - 1 	
		return vl

def cal_type_4(bits) : 
	
	if bits.get(1) == 0 : 
		return bits.get(4) , 1 
	else : 
		v = bits.get(4) 
		x = cal_type_4(bits) 
		return x[0] + v * 2 ** (4 * x[1]) , x[1] + 1 

def parse(bits) : 

	version = bits.get(3) 	
	type_id = bits.get(3) 
	version_sum = version
		
	if type_id == 4 : 
		return cal_type_4(bits)[0] , version  
	
	else : 
		ret_val = [] 
		op = OPS[type_id] 
		length_type_id = bits.get(1) 

		if length_type_id == 0 : 
			subpacket_len = bits.get(15) 
			n = bits.num_bits 
			while n - bits.num_bits < subpacket_len : 
				x , vr = parse(bits)
				version_sum += vr 
				ret_val.append(x)  
			
			return op(ret_val) , version_sum 

		else : 
			num_subpackets = bits.get(11) 		
			while num_subpackets : 
				x , vr = parse(bits)
				version_sum += vr 
				ret_val.append(x)  
				num_subpackets -= 1 

			return op(ret_val)  , version_sum


with open('16.in') as reader : 
	data = reader.read().strip() 
bits = Bits(int(data , 16) , len(data) * 4) 
print(parse(bits)) 

			

