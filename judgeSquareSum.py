'''Given a non-negative integer c, decide whether there are 
two integers a and b such that a**2 + b**2 = c.'''

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        from math import sqrt

        for a in range(int(sqrt(c) + 1)):
            b = int(sqrt(c - a**2))
            if a**2 + b**2 == c: return True
        return False


