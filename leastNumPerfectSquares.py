# problem is find least number of perfect squares that sum to that number 
# e.g., 10 has 3^2 and 1^2, so returns 2
# e.g., 12 has 2^2 and 2^2 and 2^2, so returns 3

class Solution:
    def numSquares(self, n: int) -> int:
        if n<2:
            return n
    
        squares = [0]
        while len(squares) <= n:
            squares += [min([squares[-i*i] for i in range(1,int(len(squares)**0.5)+1)]) +1]
        return squares[n]
