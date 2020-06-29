'''A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?'''

class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:
    def uniquePaths(self, rights:int, downs:int) -> int:
        from math import factorial
        total_moves = rights + downs - 2          # -2 because we are not counting getting to/from where we start/end
        right_moves,down_moves = rights-1, downs-1         # right_moves,down_moves are the total # - 1
        move_options = factorial(total_moves)//factorial(right_moves)//factorial(down_moves)
        return move_options
    
    # or you can compress the above 5 lines into 1
        return (factorial(rights+downs-2)//factorial(rights-1)//factorial(downs-1))

