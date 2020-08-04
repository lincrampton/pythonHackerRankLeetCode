'''Given an integer (signed 32 bits), write a function to check whether it is a power of 4.  So 16 is a power, as is 0.25 '''


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0 :
            return False
    
        if num >= 1:
            return not(num & (num-1)) and not(num & 0xAAAAAAAA)   # 0xAAAAAAAA has 1 in all odd spots (= 0b101010101-and-so-on) 

        # if here, 0<num>1 -> a negative power of 4
        import math
        log4 = math.log(num)/math.log(4)
        return (math.floor(log4) == log4)
        
