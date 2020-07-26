'''Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.'''


class Solution:
    def addDigits(self, num: int) -> int:
        
	# checking edge cases just slow it down
	# will only do while when num<10, so don't bother checking
        #if num<10:
            #return num
        
        while num>9:
            num = sum(int(c) for c in str(num))
        
        return num
