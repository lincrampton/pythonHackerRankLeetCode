'''Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.  You may return any answer array that satisfies this condition.'''

 
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        

        # if len(A) < 2:
        #     return A

	# although this looks cool, it is terribly inefficient
        # return ([element for element in A if element%2==0] + [element for element in A if element%2==1])
    
        odds, evens = [], []
        for n in A:
            if n%2==0:
                evens.append(n)
            else:
                odds.append(n)
        
        return (evens+odds)
